"""
    Functions to help with deinterlacing or deinterlaced content.
"""

from functools import partial
from typing import Optional

from havsfunc import QTGMC

import vapoursynth as vs

from . import util

core = vs.core


def deblend(clip: vs.VideoNode, rep: int = None) -> vs.VideoNode:
    funcname = "deblend"
    """
    A simple function to fix deblending for interlaced video with an AABBA blending pattern,
    where A is a normal frame and B is a blended frame.

    Assuming there's a constant pattern of frames (labeled A, B, C, CD, and DA in this function),
    blending can be fixed by calculating the C frame by getting halves of CD and DA, and using that
    to fix up CD. DA can then be dropped due to it being an interlaced frame.

    However, doing this will result in some of the artifacting being added to the deblended frame.
    We can mitigate this by repairing the frame with the non-blended frame before it.

    For more information, please refer to this blogpost by torchlight:
    https://mechaweaponsvidya.wordpress.com/2012/09/13/adventures-in-deblending/

    :param rep: int: Repair mode for the deblended frames
    """

    blends_a = range(2, clip.num_frames-1, 5)
    blends_b = range(3, clip.num_frames-1, 5)
    expr_cd = ["z a 2 / - y x 2 / - +"]

    def deblend(n, clip, rep):
    # Thanks Myaa, motbob and kageru!
        if n%5 in [0, 1, 4]:
            return clip
        else:
            if n in blends_a:
                c, cd, da, a = clip[n-1], clip[n], clip[n+1], clip[n+2]
                debl = core.std.Expr([c, cd, da, a], expr_cd)
                return util.pick_repair(clip)(debl, c, rep) if rep else debl
            else:
                return clip

    debl = core.std.FrameEval(clip, partial(deblend, clip=clip, rep=rep))
    return core.std.DeleteFrames(debl, blends_b).std.AssumeFPS(fpsnum=24000, fpsden=1001)


def decomb(clip: vs.VideoNode,
           TFF: Optional[bool] = None,
           decimate: bool = True,
           vinv: bool = False,
           sharpen: bool = False, dir: str = 'v',
           rep: Optional[int] = None):
    funcname = "decomb"
    """
    Function written by Midlifecrisis from the WEEB AUTISM server, and slightly modified by me.

    This function does some aggressive filtering to get rid of the combing on a interlaced/telecined source.
    You can also allow it to decimate the clip, or keep it disabled if you wish to handle the decimating yourself.
    Vinverse can also be disabled, allowing for less aggressive decombing. Note that this means far more combing will be left over!

    :param TFF: bool:           Top-Field-First. Mandatory to set. Set to either "True" or False"
    :param decimate: bool:      Decimate the video after deinterlacing
    :param vinv: bool:          Use vinverse to get rid of additional combing
    :param sharpen: bool:       Unsharpen after deinterlacing
    :param dir: str:            Directional vector. 'v' = Vertical, 'h' = Horizontal
    :param rep: int:            Repair mode for repairing the decombed frame using the original src frame
    """
    if TFF is None:
        raise ValueError(f"{funcname}: '\"TFF\" has to be set to either \"True\" or \"False\"!'")

    VFM_TFF = int(TFF)

    def _pp(n, f, clip, pp):
        return pp if f.props._Combed == 1 else clip

    clip = core.vivtc.VFM(clip, order=VFM_TFF, mode=1)
    combmask = core.comb.CombMask(clip, cthresh=1, mthresh=3)
    combmask = core.std.Maximum(combmask, threshold=250).std.Maximum(threshold=250).std.Maximum(threshold=250).std.Maximum(threshold=250)
    combmask = core.std.BoxBlur(combmask, hradius=2, vradius=2)

    qtgmc = QTGMC(clip, TFF=TFF, SourceMatch=3, Lossless=2, TR0=1, TR1=2, TR2=3, FPSDivisor=2)
    qtgmc_merged = core.std.MaskedMerge(clip, qtgmc, combmask, first_plane=True)

    decombed = core.std.FrameEval(clip, partial(_pp, clip=clip, pp=qtgmc_merged), clip)

    decombed = decombed.vinverse.Vinverse() if vinv else decombed
    decombed = dir_unsharp(decombed, dir=dir) if sharpen else decombed
    decombed = util.pick_repair(clip)(decombed, clip, rep) if rep else decombed
    return core.vivtc.VDecimate(decombed) if decimate else decombed


def dir_deshimmer(clip: vs.VideoNode, TFF: bool = True,
                  dh: bool = False,
                  transpose: bool = True,
                  show_mask: bool = False) -> vs.VideoNode:
    funcname = "dir_deshimmer"
    """
    Directional deshimmering function

    Only works (in the few instances it does, anyway) for obvious horizontal and vertical shimmering.
    Odds of success are low. But if you're desperate, it's worth a shot.

    :param dh: bool:           Interpolate to double the height of given clip beforehand
    :param TFF: bool:          Top Field First. Set to False if TFF doesn't work
    :param transpose: bool:    Transpose the clip before attempting to deshimmer
    :param show_mask: bool:    Show nnedi3's mask
    """
    clip = core.std.Transpose(clip) if transpose else clip
    deshim = core.nnedi3.nnedi3(clip, field=TFF, dh=dh, show_mask=show_mask)
    return core.std.Transpose(deshim) if transpose else deshim


def dir_unsharp(clip: vs.VideoNode,
                strength: float = 1.0,
                dir: str = 'v',
                h: float = 3.4) -> vs.VideoNode:
    funcname = "dir_unsharp"
    """
    A diff'd directional unsharpening function.
    Special thanks to thebombzen and kageru for essentially writing the bulk of this.

    Performs one-dimensional sharpening as such: "Original + (Original - blurred) * Strength"

    This particular function is recommended for SD content, specifically after deinterlacing.

    :param strength: float:        Amount to multiply blurred clip with original clip by
    :param dir: str:               Directional vector. 'v' = Vertical, 'h' = Horizontal
    :param h: float:               Sigma for knlmeans, to prevent noise from getting sharpened
    """

    dir = dir.lower()
    if dir not in ['v', 'h']:
        raise ValueError(f"{funcname}: '\"dir\" must be either \"v\" or \"h\"'")

    den = core.knlm.KNLMeansCL(clip, d=3, a=3, h=h)
    diff = core.std.MakeDiff(clip, den)

    blur_matrix = [1, 2, 1]
    blurred_clip = core.std.Convolution(den, matrix=blur_matrix, mode=dir)
    unsharp = core.std.Expr(clips=[den, blurred_clip], expr=['x y - ' + str(strength) + ' * x +', "", ""])
    return core.std.MergeDiff(unsharp, diff)
