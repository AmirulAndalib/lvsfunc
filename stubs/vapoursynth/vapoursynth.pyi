# Stop pep8 from complaining (hopefully)
# NOQA

# Ignore Flake Warnings
# flake8: noqa

# Ignore coverage
# (No coverage)

# From https://gist.github.com/pylover/7870c235867cf22817ac5b096defb768
# noinspection PyPep8
# noinspection PyPep8Naming
# noinspection PyTypeChecker
# noinspection PyAbstractClass
# noinspection PyArgumentEqualDefault
# noinspection PyArgumentList
# noinspection PyAssignmentToLoopOrWithParameter
# noinspection PyAttributeOutsideInit
# noinspection PyAugmentAssignment
# noinspection PyBroadException
# noinspection PyByteLiteral
# noinspection PyCallByClass
# noinspection PyChainedComparsons
# noinspection PyClassHasNoInit
# noinspection PyClassicStyleClass
# noinspection PyComparisonWithNone
# noinspection PyCompatibility
# noinspection PyDecorator
# noinspection PyDefaultArgument
# noinspection PyDictCreation
# noinspection PyDictDuplicateKeys
# noinspection PyDocstringTypes
# noinspection PyExceptClausesOrder
# noinspection PyExceptionInheritance
# noinspection PyFromFutureImport
# noinspection PyGlobalUndefined
# noinspection PyIncorrectDocstring
# noinspection PyInitNewSignature
# noinspection PyInterpreter
# noinspection PyListCreation
# noinspection PyMandatoryEncoding
# noinspection PyMethodFirstArgAssignment
# noinspection PyMethodMayBeStatic
# noinspection PyMethodOverriding
# noinspection PyMethodParameters
# noinspection PyMissingConstructor
# noinspection PyMissingOrEmptyDocstring
# noinspection PyNestedDecorators
# noinspection PynonAsciiChar
# noinspection PyNoneFunctionAssignment
# noinspection PyOldStyleClasses
# noinspection PyPackageRequirements
# noinspection PyPropertyAccess
# noinspection PyPropertyDefinition
# noinspection PyProtectedMember
# noinspection PyRaisingNewStyleClass
# noinspection PyRedeclaration
# noinspection PyRedundantParentheses
# noinspection PySetFunctionToLiteral
# noinspection PySimplifyBooleanCheck
# noinspection PySingleQuotedDocstring
# noinspection PyStatementEffect
# noinspection PyStringException
# noinspection PyStringFormat
# noinspection PySuperArguments
# noinspection PyTrailingSemicolon
# noinspection PyTupleAssignmentBalance
# noinspection PyTupleItemAssignment
# noinspection PyUnboundLocalVariable
# noinspection PyUnnecessaryBackslash
# noinspection PyUnreachableCode
# noinspection PyUnresolvedReferences
# noinspection PyUnusedLocal
# noinspection ReturnValueFromInit

import ctypes
import fractions
import types
import typing

T = typing.TypeVar("T")
SingleAndSequence = typing.Union[T, typing.Sequence[T]]

###
# ENUMS AND CONSTANTS
class ColorFamily(int):
    name: str
    value: int

    GRAY: typing.ClassVar['ColorFamily']
    RGB: typing.ClassVar['ColorFamily']
    YUV: typing.ClassVar['ColorFamily']
    YCOCG: typing.ClassVar['ColorFamily']
    COMPAT: typing.ClassVar['ColorFamily']

GRAY: ColorFamily
RGB: ColorFamily
YUV: ColorFamily
YCOCG: ColorFamily
COMPAT: ColorFamily


class SampleType(int):
    name: str
    value: int

    INTEGER: typing.ClassVar['SampleType']
    FLOAT: typing.ClassVar['SampleType']


INTEGER: SampleType
FLOAT: SampleType


class PresetFormat(int):
    name: str
    value: int

    NONE: typing.ClassVar['PresetFormat']

    GRAY8: typing.ClassVar['PresetFormat']
    GRAY16: typing.ClassVar['PresetFormat']

    GRAYH: typing.ClassVar['PresetFormat']
    GRAYS: typing.ClassVar['PresetFormat']

    YUV420P8: typing.ClassVar['PresetFormat']
    YUV422P8: typing.ClassVar['PresetFormat']
    YUV444P8: typing.ClassVar['PresetFormat']
    YUV410P8: typing.ClassVar['PresetFormat']
    YUV411P8: typing.ClassVar['PresetFormat']
    YUV440P8: typing.ClassVar['PresetFormat']

    YUV420P9: typing.ClassVar['PresetFormat']
    YUV422P9: typing.ClassVar['PresetFormat']
    YUV444P9: typing.ClassVar['PresetFormat']

    YUV420P10: typing.ClassVar['PresetFormat']
    YUV422P10: typing.ClassVar['PresetFormat']
    YUV444P10: typing.ClassVar['PresetFormat']

    YUV420P12: typing.ClassVar['PresetFormat']
    YUV422P12: typing.ClassVar['PresetFormat']
    YUV444P12: typing.ClassVar['PresetFormat']

    YUV420P14: typing.ClassVar['PresetFormat']
    YUV422P14: typing.ClassVar['PresetFormat']
    YUV444P14: typing.ClassVar['PresetFormat']

    YUV420P16: typing.ClassVar['PresetFormat']
    YUV422P16: typing.ClassVar['PresetFormat']
    YUV444P16: typing.ClassVar['PresetFormat']

    YUV444PH: typing.ClassVar['PresetFormat']
    YUV444PS: typing.ClassVar['PresetFormat']

    RGB24: typing.ClassVar['PresetFormat']
    RGB27: typing.ClassVar['PresetFormat']
    RGB30: typing.ClassVar['PresetFormat']
    RGB48: typing.ClassVar['PresetFormat']

    RGBH: typing.ClassVar['PresetFormat']
    RGBS: typing.ClassVar['PresetFormat']

    COMPATBGR32: typing.ClassVar['PresetFormat']
    COMPATYUY2: typing.ClassVar['PresetFormat']


NONE: PresetFormat

GRAY8: PresetFormat
GRAY16: PresetFormat

GRAYH: PresetFormat
GRAYS: PresetFormat

YUV420P8: PresetFormat
YUV422P8: PresetFormat
YUV444P8: PresetFormat
YUV410P8: PresetFormat
YUV411P8: PresetFormat
YUV440P8: PresetFormat

YUV420P9: PresetFormat
YUV422P9: PresetFormat
YUV444P9: PresetFormat

YUV420P10: PresetFormat
YUV422P10: PresetFormat
YUV444P10: PresetFormat

YUV420P12: PresetFormat
YUV422P12: PresetFormat
YUV444P12: PresetFormat

YUV420P14: PresetFormat
YUV422P14: PresetFormat
YUV444P14: PresetFormat

YUV420P16: PresetFormat
YUV422P16: PresetFormat
YUV444P16: PresetFormat

YUV444PH: PresetFormat
YUV444PS: PresetFormat

RGB24: PresetFormat
RGB27: PresetFormat
RGB30: PresetFormat
RGB48: PresetFormat

RGBH: PresetFormat
RGBS: PresetFormat

COMPATBGR32: PresetFormat
COMPATYUY2: PresetFormat


###
# VapourSynth Environment SubSystem

class EnvironmentData:
    """
    Contains the data VapourSynth stores for a specific environment.
    """


class Environment:
    alive: bool
    single: bool
    env_id: int
    active: bool

    def copy(self) -> Environment: ...
    def use(self) -> typing.ContextManager[None]: ...

    def __enter__(self) -> Environment: ...
    def __exit__(self, ty: typing.Type[BaseException], tv: BaseException, tb: types.TracebackType) -> None: ...

class EnvironmentPolicyAPI:
    def wrap_environment(self, environment_data: EnvironmentData) -> Environment: ...
    def create_environment(self) -> EnvironmentData: ...
    def unregister_policy(self) -> None: ...

class EnvironmentPolicy:
    def on_policy_registered(self, special_api: EnvironmentPolicyAPI) -> None: ...
    def on_policy_cleared(self) -> None: ...
    def get_current_environment(self) -> typing.Optional[EnvironmentData]: ...
    def set_environment(self, environment: typing.Optional[EnvironmentData]) -> None: ...
    def is_active(self, environment: EnvironmentData) -> bool: ...


_using_vsscript: bool


def register_policy(policy: EnvironmentPolicy) -> None: ...
def has_policy() -> bool: ...

def vpy_current_environment() -> Environment: ...
def get_current_environment() -> Environment: ...


class AlphaOutputTuple(typing.NamedTuple):
    clip: 'VideoNode'
    alpha: 'VideoNode'

Func = typing.Callable[..., typing.Any]

class Error(Exception): ...

def set_message_handler(handler_func: typing.Callable[[int, str], None]) -> None: ...
def clear_output(index: int = 0) -> None: ...
def clear_outputs() -> None: ...
def get_outputs() -> typing.Mapping[int, typing.Union['VideoNode', AlphaOutputTuple]]: ...
def get_output(index: int = 0) -> typing.Union['VideoNode', AlphaOutputTuple]: ...


class Format:
    id: int
    name: str
    color_family: ColorFamily
    sample_type: SampleType
    bits_per_sample: int
    bytes_per_sample: int
    subsampling_w: int
    subsampling_h: int
    num_planes: int

    def _as_dict(self) -> typing.Dict[str, typing.Any]: ...
    def replace(self, *,
                color_family: typing.Optional[ColorFamily] = None,
                sample_type: typing.Optional[SampleType] = None,
                bits_per_sample: typing.Optional[int] = None,
                subsampling_w: typing.Optional[int] = None,
                subsampling_h: typing.Optional[int] = None
                ) -> 'Format': ...


_VideoPropsValue = typing.Union[
    SingleAndSequence[int],
    SingleAndSequence[float],
    SingleAndSequence[str],
    SingleAndSequence['VideoNode'],
    SingleAndSequence['VideoFrame'],
    SingleAndSequence[typing.Callable[..., typing.Any]]
]

class VideoProps(typing.MutableMapping[str, _VideoPropsValue]):
    def __getattr__(self, name: str) -> _VideoPropsValue: ...
    def __setattr__(self, name: str, value: _VideoPropsValue) -> None: ...

    # mypy lo vult.
    # In all seriousness, why do I need to manually define them in a typestub?
    def __delitem__(self, name: str) -> None: ...
    def __setitem__(self, name: str, value: _VideoPropsValue) -> None: ...
    def __getitem__(self, name: str) -> _VideoPropsValue: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __len__(self) -> int: ...

class VideoPlane:
    width: int
    height: int


class VideoFrame:
    props: VideoProps
    height: int
    width: int
    format: Format
    readonly: bool

    def copy(self) -> 'VideoFrame': ...

    def get_read_ptr(self, plane: int) -> ctypes.c_void_p: ...
    def get_read_array(self, plane: int) -> typing.Optional[memoryview]: ...
    def get_write_ptr(self, plane: int) -> ctypes.c_void_p: ...
    def get_write_array(self, plane: int) -> typing.Optional[memoryview]: ...

    def get_stride(self, plane: int) -> int: ...
    def planes(self) -> typing.Iterator['VideoPlane']: ...


class _Future(typing.Generic[T]):
    def set_result(self, value: T) -> None: ...
    def set_exception(self, exception: BaseException) -> None: ...
    def result(self) -> T: ...
    def exception(self) -> typing.Optional[typing.NoReturn]: ...


class Plugin:
    namespace: str

    def get_functions(self) -> typing.Dict[str, str]: ...
    def list_functions(self) -> str: ...


# implementation: adg
class _Plugin_adg_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Mask(self, clip: "VideoNode", luma_scaling: typing.Optional[float] = None) -> "VideoNode": ...


class _Plugin_adg_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Mask(self, luma_scaling: typing.Optional[float] = None) -> "VideoNode": ...
# end implementation


# implementation: bilateral
class _Plugin_bilateral_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bilateral(self, input: "VideoNode", ref: typing.Optional["VideoNode"] = None, sigmaS: typing.Optional[SingleAndSequence[float]] = None, sigmaR: typing.Optional[SingleAndSequence[float]] = None, planes: typing.Optional[SingleAndSequence[int]] = None, algorithm: typing.Optional[SingleAndSequence[int]] = None, PBFICnum: typing.Optional[SingleAndSequence[int]] = None) -> "VideoNode": ...
    def Gaussian(self, input: "VideoNode", sigma: typing.Optional[SingleAndSequence[float]] = None, sigmaV: typing.Optional[SingleAndSequence[float]] = None) -> "VideoNode": ...


class _Plugin_bilateral_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bilateral(self, ref: typing.Optional["VideoNode"] = None, sigmaS: typing.Optional[SingleAndSequence[float]] = None, sigmaR: typing.Optional[SingleAndSequence[float]] = None, planes: typing.Optional[SingleAndSequence[int]] = None, algorithm: typing.Optional[SingleAndSequence[int]] = None, PBFICnum: typing.Optional[SingleAndSequence[int]] = None) -> "VideoNode": ...
    def Gaussian(self, sigma: typing.Optional[SingleAndSequence[float]] = None, sigmaV: typing.Optional[SingleAndSequence[float]] = None) -> "VideoNode": ...
# end implementation


# implementation: bm3d
class _Plugin_bm3d_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Basic(self, input: "VideoNode", ref: typing.Optional["VideoNode"] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, hard_thr: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def Final(self, input: "VideoNode", ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def OPP2RGB(self, input: "VideoNode", sample: typing.Optional[int] = None) -> "VideoNode": ...
    def RGB2OPP(self, input: "VideoNode", sample: typing.Optional[int] = None) -> "VideoNode": ...
    def VAggregate(self, input: "VideoNode", radius: typing.Optional[int] = None, sample: typing.Optional[int] = None) -> "VideoNode": ...
    def VBasic(self, input: "VideoNode", ref: typing.Optional["VideoNode"] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, radius: typing.Optional[int] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, ps_num: typing.Optional[int] = None, ps_range: typing.Optional[int] = None, ps_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, hard_thr: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def VFinal(self, input: "VideoNode", ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, radius: typing.Optional[int] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, ps_num: typing.Optional[int] = None, ps_range: typing.Optional[int] = None, ps_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_bm3d_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Basic(self, ref: typing.Optional["VideoNode"] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, hard_thr: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def Final(self, ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def OPP2RGB(self, sample: typing.Optional[int] = None) -> "VideoNode": ...
    def RGB2OPP(self, sample: typing.Optional[int] = None) -> "VideoNode": ...
    def VAggregate(self, radius: typing.Optional[int] = None, sample: typing.Optional[int] = None) -> "VideoNode": ...
    def VBasic(self, ref: typing.Optional["VideoNode"] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, radius: typing.Optional[int] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, ps_num: typing.Optional[int] = None, ps_range: typing.Optional[int] = None, ps_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, hard_thr: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
    def VFinal(self, ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[float, typing.Sequence[float], None] = None, radius: typing.Optional[int] = None, block_size: typing.Optional[int] = None, block_step: typing.Optional[int] = None, group_size: typing.Optional[int] = None, bm_range: typing.Optional[int] = None, bm_step: typing.Optional[int] = None, ps_num: typing.Optional[int] = None, ps_range: typing.Optional[int] = None, ps_step: typing.Optional[int] = None, th_mse: typing.Optional[float] = None, matrix: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: comb
class _Plugin_comb_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def CMaskedMerge(self, base: "VideoNode", alt: "VideoNode", mask: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def CombMask(self, clip: "VideoNode", cthresh: typing.Optional[int] = None, mthresh: typing.Optional[int] = None, mi: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_comb_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def CMaskedMerge(self, alt: "VideoNode", mask: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def CombMask(self, cthresh: typing.Optional[int] = None, mthresh: typing.Optional[int] = None, mi: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
# end implementation


# implementation: d2v
class _Plugin_d2v_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ApplyRFF(self, clip: "VideoNode", d2v: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def Source(self, input: typing.Union[str, bytes, bytearray], threads: typing.Optional[int] = None, nocrop: typing.Optional[int] = None, rff: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_d2v_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ApplyRFF(self, d2v: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def Source(self, threads: typing.Optional[int] = None, nocrop: typing.Optional[int] = None, rff: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: descale
class _Plugin_descale_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Debicubic(self, src: "VideoNode", width: int, height: int, b: typing.Optional[float] = None, c: typing.Optional[float] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Debilinear(self, src: "VideoNode", width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Delanczos(self, src: "VideoNode", width: int, height: int, taps: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline16(self, src: "VideoNode", width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline36(self, src: "VideoNode", width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline64(self, src: "VideoNode", width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...


class _Plugin_descale_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Debicubic(self, width: int, height: int, b: typing.Optional[float] = None, c: typing.Optional[float] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Debilinear(self, width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Delanczos(self, width: int, height: int, taps: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline16(self, width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline36(self, width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
    def Despline64(self, width: int, height: int, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None) -> "VideoNode": ...
# end implementation


# implementation: dfttest
class _Plugin_dfttest_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DFTTest(self, clip: "VideoNode", ftype: typing.Optional[int] = None, sigma: typing.Optional[float] = None, sigma2: typing.Optional[float] = None, pmin: typing.Optional[float] = None, pmax: typing.Optional[float] = None, sbsize: typing.Optional[int] = None, smode: typing.Optional[int] = None, sosize: typing.Optional[int] = None, tbsize: typing.Optional[int] = None, tmode: typing.Optional[int] = None, tosize: typing.Optional[int] = None, swin: typing.Optional[int] = None, twin: typing.Optional[int] = None, sbeta: typing.Optional[float] = None, tbeta: typing.Optional[float] = None, zmean: typing.Optional[int] = None, f0beta: typing.Optional[float] = None, nlocation: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, slocation: typing.Union[float, typing.Sequence[float], None] = None, ssx: typing.Union[float, typing.Sequence[float], None] = None, ssy: typing.Union[float, typing.Sequence[float], None] = None, sst: typing.Union[float, typing.Sequence[float], None] = None, ssystem: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, opt: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_dfttest_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DFTTest(self, ftype: typing.Optional[int] = None, sigma: typing.Optional[float] = None, sigma2: typing.Optional[float] = None, pmin: typing.Optional[float] = None, pmax: typing.Optional[float] = None, sbsize: typing.Optional[int] = None, smode: typing.Optional[int] = None, sosize: typing.Optional[int] = None, tbsize: typing.Optional[int] = None, tmode: typing.Optional[int] = None, tosize: typing.Optional[int] = None, swin: typing.Optional[int] = None, twin: typing.Optional[int] = None, sbeta: typing.Optional[float] = None, tbeta: typing.Optional[float] = None, zmean: typing.Optional[int] = None, f0beta: typing.Optional[float] = None, nlocation: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, slocation: typing.Union[float, typing.Sequence[float], None] = None, ssx: typing.Union[float, typing.Sequence[float], None] = None, ssy: typing.Union[float, typing.Sequence[float], None] = None, sst: typing.Union[float, typing.Sequence[float], None] = None, ssystem: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, opt: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: dgdecodenv
class _Plugin_dgdecodenv_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DGSource(self, source: typing.Union[str, bytes, bytearray], i420: typing.Optional[int] = None, deinterlace: typing.Optional[int] = None, use_top_field: typing.Optional[int] = None, use_pf: typing.Optional[int] = None, ct: typing.Optional[int] = None, cb: typing.Optional[int] = None, cl: typing.Optional[int] = None, cr: typing.Optional[int] = None, rw: typing.Optional[int] = None, rh: typing.Optional[int] = None, fieldop: typing.Optional[int] = None, show: typing.Optional[int] = None, show2: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_dgdecodenv_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DGSource(self, i420: typing.Optional[int] = None, deinterlace: typing.Optional[int] = None, use_top_field: typing.Optional[int] = None, use_pf: typing.Optional[int] = None, ct: typing.Optional[int] = None, cb: typing.Optional[int] = None, cl: typing.Optional[int] = None, cr: typing.Optional[int] = None, rw: typing.Optional[int] = None, rh: typing.Optional[int] = None, fieldop: typing.Optional[int] = None, show: typing.Optional[int] = None, show2: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
# end implementation


# implementation: edgefixer
class _Plugin_edgefixer_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ContinuityFixer(self, clip: "VideoNode", left: SingleAndSequence[int], top: SingleAndSequence[int], right: SingleAndSequence[int], bottom: SingleAndSequence[int], radius: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_edgefixer_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ContinuityFixer(self, left: SingleAndSequence[int], top: SingleAndSequence[int], right: SingleAndSequence[int], bottom: SingleAndSequence[int], radius: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
# end implementation


# implementation: eedi3m
class _Plugin_eedi3m_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def EEDI3(self, clip: "VideoNode", field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, beta: typing.Optional[float] = None, gamma: typing.Optional[float] = None, nrad: typing.Optional[int] = None, mdis: typing.Optional[int] = None, hp: typing.Optional[int] = None, ucubic: typing.Optional[int] = None, cost3: typing.Optional[int] = None, vcheck: typing.Optional[int] = None, vthresh0: typing.Optional[float] = None, vthresh1: typing.Optional[float] = None, vthresh2: typing.Optional[float] = None, sclip: typing.Optional["VideoNode"] = None, mclip: typing.Optional["VideoNode"] = None, opt: typing.Optional[int] = None) -> "VideoNode": ...
    def EEDI3CL(self, clip: "VideoNode", field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, beta: typing.Optional[float] = None, gamma: typing.Optional[float] = None, nrad: typing.Optional[int] = None, mdis: typing.Optional[int] = None, hp: typing.Optional[int] = None, ucubic: typing.Optional[int] = None, cost3: typing.Optional[int] = None, vcheck: typing.Optional[int] = None, vthresh0: typing.Optional[float] = None, vthresh1: typing.Optional[float] = None, vthresh2: typing.Optional[float] = None, sclip: typing.Optional["VideoNode"] = None, opt: typing.Optional[int] = None, device: typing.Optional[int] = None, list_device: typing.Optional[int] = None, info: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_eedi3m_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def EEDI3(self, field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, beta: typing.Optional[float] = None, gamma: typing.Optional[float] = None, nrad: typing.Optional[int] = None, mdis: typing.Optional[int] = None, hp: typing.Optional[int] = None, ucubic: typing.Optional[int] = None, cost3: typing.Optional[int] = None, vcheck: typing.Optional[int] = None, vthresh0: typing.Optional[float] = None, vthresh1: typing.Optional[float] = None, vthresh2: typing.Optional[float] = None, sclip: typing.Optional["VideoNode"] = None, mclip: typing.Optional["VideoNode"] = None, opt: typing.Optional[int] = None) -> "VideoNode": ...
    def EEDI3CL(self, field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, alpha: typing.Optional[float] = None, beta: typing.Optional[float] = None, gamma: typing.Optional[float] = None, nrad: typing.Optional[int] = None, mdis: typing.Optional[int] = None, hp: typing.Optional[int] = None, ucubic: typing.Optional[int] = None, cost3: typing.Optional[int] = None, vcheck: typing.Optional[int] = None, vthresh0: typing.Optional[float] = None, vthresh1: typing.Optional[float] = None, vthresh2: typing.Optional[float] = None, sclip: typing.Optional["VideoNode"] = None, opt: typing.Optional[int] = None, device: typing.Optional[int] = None, list_device: typing.Optional[int] = None, info: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: ffms2
class _Plugin_ffms2_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def GetLogLevel(self) -> "VideoNode": ...
    def Index(self, source: typing.Union[str, bytes, bytearray], cachefile: typing.Union[str, bytes, bytearray, None] = None, indextracks: typing.Union[int, typing.Sequence[int], None] = None, dumptracks: typing.Union[int, typing.Sequence[int], None] = None, audiofile: typing.Union[str, bytes, bytearray, None] = None, errorhandling: typing.Optional[int] = None, overwrite: typing.Optional[int] = None, demuxer: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def SetLogLevel(self, level: int) -> "VideoNode": ...
    def Source(self, source: typing.Union[str, bytes, bytearray], track: typing.Optional[int] = None, cache: typing.Optional[int] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, threads: typing.Optional[int] = None, timecodes: typing.Union[str, bytes, bytearray, None] = None, seekmode: typing.Optional[int] = None, width: typing.Optional[int] = None, height: typing.Optional[int] = None, resizer: typing.Union[str, bytes, bytearray, None] = None, format: typing.Optional[int] = None, alpha: typing.Optional[int] = None) -> "VideoNode": ...
    def Version(self) -> "VideoNode": ...


class _Plugin_ffms2_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def GetLogLevel(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Optional["VideoNode"]: ...
    def Index(self, cachefile: typing.Union[str, bytes, bytearray, None] = None, indextracks: typing.Union[int, typing.Sequence[int], None] = None, dumptracks: typing.Union[int, typing.Sequence[int], None] = None, audiofile: typing.Union[str, bytes, bytearray, None] = None, errorhandling: typing.Optional[int] = None, overwrite: typing.Optional[int] = None, demuxer: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def SetLogLevel(self) -> "VideoNode": ...
    def Source(self, track: typing.Optional[int] = None, cache: typing.Optional[int] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, threads: typing.Optional[int] = None, timecodes: typing.Union[str, bytes, bytearray, None] = None, seekmode: typing.Optional[int] = None, width: typing.Optional[int] = None, height: typing.Optional[int] = None, resizer: typing.Union[str, bytes, bytearray, None] = None, format: typing.Optional[int] = None, alpha: typing.Optional[int] = None) -> "VideoNode": ...
    def Version(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Optional["VideoNode"]: ...
# end implementation


# implementation: fmtc
class _Plugin_fmtc_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def bitdepth(self, clip: "VideoNode", csp: typing.Optional[int] = None, bits: typing.Optional[int] = None, flt: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, dmode: typing.Optional[int] = None, ampo: typing.Optional[float] = None, ampn: typing.Optional[float] = None, dyn: typing.Optional[int] = None, staticnoise: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None, patsize: typing.Optional[int] = None) -> "VideoNode": ...
    def histluma(self, clip: "VideoNode", full: typing.Optional[int] = None, amp: typing.Optional[int] = None) -> "VideoNode": ...
    def matrix(self, clip: "VideoNode", mat: typing.Union[str, bytes, bytearray, None] = None, mats: typing.Union[str, bytes, bytearray, None] = None, matd: typing.Union[str, bytes, bytearray, None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, coef: typing.Union[float, typing.Sequence[float], None] = None, csp: typing.Optional[int] = None, col_fam: typing.Optional[int] = None, bits: typing.Optional[int] = None, singleout: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def matrix2020cl(self, clip: "VideoNode", full: typing.Optional[int] = None, csp: typing.Optional[int] = None, bits: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def nativetostack16(self, clip: "VideoNode") -> "VideoNode": ...
    def primaries(self, clip: "VideoNode", rs: typing.Union[float, typing.Sequence[float], None] = None, gs: typing.Union[float, typing.Sequence[float], None] = None, bs: typing.Union[float, typing.Sequence[float], None] = None, ws: typing.Union[float, typing.Sequence[float], None] = None, rd: typing.Union[float, typing.Sequence[float], None] = None, gd: typing.Union[float, typing.Sequence[float], None] = None, bd: typing.Union[float, typing.Sequence[float], None] = None, wd: typing.Union[float, typing.Sequence[float], None] = None, prims: typing.Union[str, bytes, bytearray, None] = None, primd: typing.Union[str, bytes, bytearray, None] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def resample(self, clip: "VideoNode", w: typing.Optional[int] = None, h: typing.Optional[int] = None, sx: typing.Union[float, typing.Sequence[float], None] = None, sy: typing.Union[float, typing.Sequence[float], None] = None, sw: typing.Union[float, typing.Sequence[float], None] = None, sh: typing.Union[float, typing.Sequence[float], None] = None, scale: typing.Optional[float] = None, scaleh: typing.Optional[float] = None, scalev: typing.Optional[float] = None, kernel: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelh: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelv: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, impulse: typing.Union[float, typing.Sequence[float], None] = None, impulseh: typing.Union[float, typing.Sequence[float], None] = None, impulsev: typing.Union[float, typing.Sequence[float], None] = None, taps: typing.Union[int, typing.Sequence[int], None] = None, tapsh: typing.Union[int, typing.Sequence[int], None] = None, tapsv: typing.Union[int, typing.Sequence[int], None] = None, a1: typing.Union[float, typing.Sequence[float], None] = None, a2: typing.Union[float, typing.Sequence[float], None] = None, a3: typing.Union[float, typing.Sequence[float], None] = None, kovrspl: typing.Union[int, typing.Sequence[int], None] = None, fh: typing.Union[float, typing.Sequence[float], None] = None, fv: typing.Union[float, typing.Sequence[float], None] = None, cnorm: typing.Union[int, typing.Sequence[int], None] = None, totalh: typing.Union[float, typing.Sequence[float], None] = None, totalv: typing.Union[float, typing.Sequence[float], None] = None, invks: typing.Union[int, typing.Sequence[int], None] = None, invksh: typing.Union[int, typing.Sequence[int], None] = None, invksv: typing.Union[int, typing.Sequence[int], None] = None, invkstaps: typing.Union[int, typing.Sequence[int], None] = None, invkstapsh: typing.Union[int, typing.Sequence[int], None] = None, invkstapsv: typing.Union[int, typing.Sequence[int], None] = None, csp: typing.Optional[int] = None, css: typing.Union[str, bytes, bytearray, None] = None, planes: typing.Union[float, typing.Sequence[float], None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, center: typing.Union[int, typing.Sequence[int], None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None, cplaces: typing.Union[str, bytes, bytearray, None] = None, cplaced: typing.Union[str, bytes, bytearray, None] = None, interlaced: typing.Optional[int] = None, interlacedd: typing.Optional[int] = None, tff: typing.Optional[int] = None, tffd: typing.Optional[int] = None, flt: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def stack16tonative(self, clip: "VideoNode") -> "VideoNode": ...
    def transfer(self, clip: "VideoNode", transs: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, transd: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, cont: typing.Optional[float] = None, gcor: typing.Optional[float] = None, bits: typing.Optional[int] = None, flt: typing.Optional[int] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None, blacklvl: typing.Optional[float] = None) -> "VideoNode": ...


class _Plugin_fmtc_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def bitdepth(self, csp: typing.Optional[int] = None, bits: typing.Optional[int] = None, flt: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, dmode: typing.Optional[int] = None, ampo: typing.Optional[float] = None, ampn: typing.Optional[float] = None, dyn: typing.Optional[int] = None, staticnoise: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None, patsize: typing.Optional[int] = None) -> "VideoNode": ...
    def histluma(self, full: typing.Optional[int] = None, amp: typing.Optional[int] = None) -> "VideoNode": ...
    def matrix(self, mat: typing.Union[str, bytes, bytearray, None] = None, mats: typing.Union[str, bytes, bytearray, None] = None, matd: typing.Union[str, bytes, bytearray, None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, coef: typing.Union[float, typing.Sequence[float], None] = None, csp: typing.Optional[int] = None, col_fam: typing.Optional[int] = None, bits: typing.Optional[int] = None, singleout: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def matrix2020cl(self, full: typing.Optional[int] = None, csp: typing.Optional[int] = None, bits: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def nativetostack16(self) -> "VideoNode": ...
    def primaries(self, rs: typing.Union[float, typing.Sequence[float], None] = None, gs: typing.Union[float, typing.Sequence[float], None] = None, bs: typing.Union[float, typing.Sequence[float], None] = None, ws: typing.Union[float, typing.Sequence[float], None] = None, rd: typing.Union[float, typing.Sequence[float], None] = None, gd: typing.Union[float, typing.Sequence[float], None] = None, bd: typing.Union[float, typing.Sequence[float], None] = None, wd: typing.Union[float, typing.Sequence[float], None] = None, prims: typing.Union[str, bytes, bytearray, None] = None, primd: typing.Union[str, bytes, bytearray, None] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def resample(self, w: typing.Optional[int] = None, h: typing.Optional[int] = None, sx: typing.Union[float, typing.Sequence[float], None] = None, sy: typing.Union[float, typing.Sequence[float], None] = None, sw: typing.Union[float, typing.Sequence[float], None] = None, sh: typing.Union[float, typing.Sequence[float], None] = None, scale: typing.Optional[float] = None, scaleh: typing.Optional[float] = None, scalev: typing.Optional[float] = None, kernel: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelh: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelv: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, impulse: typing.Union[float, typing.Sequence[float], None] = None, impulseh: typing.Union[float, typing.Sequence[float], None] = None, impulsev: typing.Union[float, typing.Sequence[float], None] = None, taps: typing.Union[int, typing.Sequence[int], None] = None, tapsh: typing.Union[int, typing.Sequence[int], None] = None, tapsv: typing.Union[int, typing.Sequence[int], None] = None, a1: typing.Union[float, typing.Sequence[float], None] = None, a2: typing.Union[float, typing.Sequence[float], None] = None, a3: typing.Union[float, typing.Sequence[float], None] = None, kovrspl: typing.Union[int, typing.Sequence[int], None] = None, fh: typing.Union[float, typing.Sequence[float], None] = None, fv: typing.Union[float, typing.Sequence[float], None] = None, cnorm: typing.Union[int, typing.Sequence[int], None] = None, totalh: typing.Union[float, typing.Sequence[float], None] = None, totalv: typing.Union[float, typing.Sequence[float], None] = None, invks: typing.Union[int, typing.Sequence[int], None] = None, invksh: typing.Union[int, typing.Sequence[int], None] = None, invksv: typing.Union[int, typing.Sequence[int], None] = None, invkstaps: typing.Union[int, typing.Sequence[int], None] = None, invkstapsh: typing.Union[int, typing.Sequence[int], None] = None, invkstapsv: typing.Union[int, typing.Sequence[int], None] = None, csp: typing.Optional[int] = None, css: typing.Union[str, bytes, bytearray, None] = None, planes: typing.Union[float, typing.Sequence[float], None] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, center: typing.Union[int, typing.Sequence[int], None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None, cplaces: typing.Union[str, bytes, bytearray, None] = None, cplaced: typing.Union[str, bytes, bytearray, None] = None, interlaced: typing.Optional[int] = None, interlacedd: typing.Optional[int] = None, tff: typing.Optional[int] = None, tffd: typing.Optional[int] = None, flt: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None) -> "VideoNode": ...
    def stack16tonative(self) -> "VideoNode": ...
    def transfer(self, transs: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, transd: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, cont: typing.Optional[float] = None, gcor: typing.Optional[float] = None, bits: typing.Optional[int] = None, flt: typing.Optional[int] = None, fulls: typing.Optional[int] = None, fulld: typing.Optional[int] = None, cpuopt: typing.Optional[int] = None, blacklvl: typing.Optional[float] = None) -> "VideoNode": ...
# end implementation


# implementation: imwri
class _Plugin_imwri_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, filename: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]]], firstnum: typing.Optional[int] = None, mismatch: typing.Optional[int] = None, alpha: typing.Optional[int] = None, float_output: typing.Optional[int] = None) -> "VideoNode": ...
    def Write(self, clip: "VideoNode", imgformat: typing.Union[str, bytes, bytearray], filename: typing.Union[str, bytes, bytearray], firstnum: typing.Optional[int] = None, quality: typing.Optional[int] = None, dither: typing.Optional[int] = None, compression_type: typing.Union[str, bytes, bytearray, None] = None, overwrite: typing.Optional[int] = None, alpha: typing.Optional["VideoNode"] = None) -> "VideoNode": ...


class _Plugin_imwri_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, firstnum: typing.Optional[int] = None, mismatch: typing.Optional[int] = None, alpha: typing.Optional[int] = None, float_output: typing.Optional[int] = None) -> "VideoNode": ...
    def Write(self, imgformat: typing.Union[str, bytes, bytearray], filename: typing.Union[str, bytes, bytearray], firstnum: typing.Optional[int] = None, quality: typing.Optional[int] = None, dither: typing.Optional[int] = None, compression_type: typing.Union[str, bytes, bytearray, None] = None, overwrite: typing.Optional[int] = None, alpha: typing.Optional["VideoNode"] = None) -> "VideoNode": ...
# end implementation


# implementation: knlm
class _Plugin_knlm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def KNLMeansCL(self, clip: "VideoNode", d: typing.Optional[int] = None, a: typing.Optional[int] = None, s: typing.Optional[int] = None, h: typing.Optional[float] = None, channels: typing.Union[str, bytes, bytearray, None] = None, wmode: typing.Optional[int] = None, wref: typing.Optional[float] = None, rclip: typing.Optional["VideoNode"] = None, device_type: typing.Union[str, bytes, bytearray, None] = None, device_id: typing.Optional[int] = None, ocl_x: typing.Optional[int] = None, ocl_y: typing.Optional[int] = None, ocl_r: typing.Optional[int] = None, info: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_knlm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def KNLMeansCL(self, d: typing.Optional[int] = None, a: typing.Optional[int] = None, s: typing.Optional[int] = None, h: typing.Optional[float] = None, channels: typing.Union[str, bytes, bytearray, None] = None, wmode: typing.Optional[int] = None, wref: typing.Optional[float] = None, rclip: typing.Optional["VideoNode"] = None, device_type: typing.Union[str, bytes, bytearray, None] = None, device_id: typing.Optional[int] = None, ocl_x: typing.Optional[int] = None, ocl_y: typing.Optional[int] = None, ocl_r: typing.Optional[int] = None, info: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: lsmas
class _Plugin_lsmas_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def LWLibavSource(self, source: typing.Union[str, bytes, bytearray], stream_index: typing.Optional[int] = None, cache: typing.Optional[int] = None, threads: typing.Optional[int] = None, seek_mode: typing.Optional[int] = None, seek_threshold: typing.Optional[int] = None, dr: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, variable: typing.Optional[int] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, repeat: typing.Optional[int] = None, dominance: typing.Optional[int] = None) -> "VideoNode": ...
    def LibavSMASHSource(self, source: typing.Union[str, bytes, bytearray], track: typing.Optional[int] = None, threads: typing.Optional[int] = None, seek_mode: typing.Optional[int] = None, seek_threshold: typing.Optional[int] = None, dr: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, variable: typing.Optional[int] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_lsmas_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def LWLibavSource(self, stream_index: typing.Optional[int] = None, cache: typing.Optional[int] = None, threads: typing.Optional[int] = None, seek_mode: typing.Optional[int] = None, seek_threshold: typing.Optional[int] = None, dr: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, variable: typing.Optional[int] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, repeat: typing.Optional[int] = None, dominance: typing.Optional[int] = None) -> "VideoNode": ...
    def LibavSMASHSource(self, track: typing.Optional[int] = None, threads: typing.Optional[int] = None, seek_mode: typing.Optional[int] = None, seek_threshold: typing.Optional[int] = None, dr: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, variable: typing.Optional[int] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
# end implementation


# implementation: mpls
MPLS = typing.TypedDict("MPLS", {"clip": typing.Sequence[bytes], "filename": typing.Sequence[bytes], "count": int})
class _Plugin_mpls_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, bd_path: typing.Union[str, bytes, bytearray], playlist: int, angle: typing.Optional[int] = None) -> MPLS: ...


class _Plugin_mpls_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, playlist: int, angle: typing.Optional[int] = None) -> MPLS: ...
# end implementation


# implementation: nnedi3
class _Plugin_nnedi3_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, clip: "VideoNode", field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, nsize: typing.Optional[int] = None, nns: typing.Optional[int] = None, qual: typing.Optional[int] = None, etype: typing.Optional[int] = None, pscrn: typing.Optional[int] = None, opt: typing.Optional[int] = None, int16_prescreener: typing.Optional[int] = None, int16_predictor: typing.Optional[int] = None, exp: typing.Optional[int] = None, show_mask: typing.Optional[int] = None, combed_only: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_nnedi3_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, nsize: typing.Optional[int] = None, nns: typing.Optional[int] = None, qual: typing.Optional[int] = None, etype: typing.Optional[int] = None, pscrn: typing.Optional[int] = None, opt: typing.Optional[int] = None, int16_prescreener: typing.Optional[int] = None, int16_predictor: typing.Optional[int] = None, exp: typing.Optional[int] = None, show_mask: typing.Optional[int] = None, combed_only: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: nnedi3cl
class _Plugin_nnedi3cl_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def NNEDI3CL(self, clip: "VideoNode", field: int, dh: typing.Union[int, None] = None, dw: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, device: typing.Union[int, None] = None, list_device: typing.Union[int, None] = None, info: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_nnedi3cl_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def NNEDI3CL(self, field: int, dh: typing.Union[int, None] = None, dw: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, device: typing.Union[int, None] = None, list_device: typing.Union[int, None] = None, info: typing.Union[int, None] = None) -> "VideoNode": ...
# end implementation


# implementation: resize
class _Plugin_resize_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bicubic(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Bilinear(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Lanczos(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Point(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline16(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline36(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline64(self, clip: "VideoNode", width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...


class _Plugin_resize_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bicubic(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Bilinear(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Lanczos(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Point(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline16(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline36(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
    def Spline64(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, matrix: typing.Optional[int] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Optional[int] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Optional[int] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Optional[int] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Optional[int] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Optional[int] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Optional[int] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Optional[int] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Optional[int] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Optional[int] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Optional[float] = None, filter_param_b: typing.Optional[float] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Optional[float] = None, filter_param_b_uv: typing.Optional[float] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Optional[int] = None, src_left: typing.Optional[float] = None, src_top: typing.Optional[float] = None, src_width: typing.Optional[float] = None, src_height: typing.Optional[float] = None, nominal_luminance: typing.Optional[float] = None) -> "VideoNode": ...
# end implementation


# implementation: retinex
class _Plugin_retinex_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSRCP(self, input: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, chroma_protect: typing.Union[float, None] = None) -> "VideoNode": ...
    def MSRCR(self, input: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, restore: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_retinex_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSRCP(self, sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, chroma_protect: typing.Union[float, None] = None) -> "VideoNode": ...
    def MSRCR(self, sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, restore: typing.Union[float, None] = None) -> "VideoNode": ...
# end implementation


# implementation: rgsf
class _Plugin_rgsf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, clip: "VideoNode", previous: typing.Optional["VideoNode"] = None, next: typing.Optional["VideoNode"] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, clip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Repair(self, clip: "VideoNode", repairclip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def VerticalCleaner(self, clip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...


class _Plugin_rgsf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, previous: typing.Optional["VideoNode"] = None, next: typing.Optional["VideoNode"] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Repair(self, repairclip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def VerticalCleaner(self, mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
# end implementation


# implementation: rgvs
class _Plugin_rgvs_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, clip: "VideoNode", previous: typing.Optional["VideoNode"] = None, next: typing.Optional["VideoNode"] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, clip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Repair(self, clip: "VideoNode", repairclip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def VerticalCleaner(self, clip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...


class _Plugin_rgvs_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, previous: typing.Optional["VideoNode"] = None, next: typing.Optional["VideoNode"] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Repair(self, repairclip: "VideoNode", mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def VerticalCleaner(self, mode: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
# end implementation


# implementation: std
class _Plugin_std_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AddBorders(self, clip: "VideoNode", left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None, color: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def AssumeFPS(self, clip: "VideoNode", src: typing.Optional["VideoNode"] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None) -> "VideoNode": ...
    def Binarize(self, clip: "VideoNode", threshold: typing.Union[float, typing.Sequence[float], None] = None, v0: typing.Union[float, typing.Sequence[float], None] = None, v1: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def BlankClip(self, clip: typing.Optional["VideoNode"] = None, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, length: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, color: typing.Union[float, typing.Sequence[float], None] = None, keep: typing.Optional[int] = None) -> "VideoNode": ...
    def BoxBlur(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, hradius: typing.Optional[int] = None, hpasses: typing.Optional[int] = None, vradius: typing.Optional[int] = None, vpasses: typing.Optional[int] = None) -> "VideoNode": ...
    def Cache(self, clip: "VideoNode", size: typing.Optional[int] = None, fixed: typing.Optional[int] = None, make_linear: typing.Optional[int] = None) -> "VideoNode": ...
    def ClipToProp(self, clip: "VideoNode", mclip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Convolution(self, clip: "VideoNode", matrix: typing.Union[float, typing.Sequence[float]], bias: typing.Optional[float] = None, divisor: typing.Optional[float] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, saturate: typing.Optional[int] = None, mode: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Crop(self, clip: "VideoNode", left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None) -> "VideoNode": ...
    def CropAbs(self, clip: "VideoNode", width: int, height: int, left: typing.Optional[int] = None, top: typing.Optional[int] = None, x: typing.Optional[int] = None, y: typing.Optional[int] = None) -> "VideoNode": ...
    def CropRel(self, clip: "VideoNode", left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None) -> "VideoNode": ...
    def Deflate(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None) -> "VideoNode": ...
    def DeleteFrames(self, clip: "VideoNode", frames: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def DoubleWeave(self, clip: "VideoNode", tff: typing.Optional[int] = None) -> "VideoNode": ...
    def DuplicateFrames(self, clip: "VideoNode", frames: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Expr(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], expr: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]]], format: typing.Optional[int] = None) -> "VideoNode": ...
    def FlipHorizontal(self, clip: "VideoNode") -> "VideoNode": ...
    def FlipVertical(self, clip: "VideoNode") -> "VideoNode": ...
    def FrameEval(self, clip: "VideoNode", eval: typing.Callable[..., typing.Any], prop_src: typing.Union["VideoNode", typing.Sequence["VideoNode"], None] = None) -> "VideoNode": ...
    def FreezeFrames(self, clip: "VideoNode", first: typing.Union[int, typing.Sequence[int]], last: typing.Union[int, typing.Sequence[int]], replacement: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Inflate(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None) -> "VideoNode": ...
    def Interleave(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], extend: typing.Optional[int] = None, mismatch: typing.Optional[int] = None, modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def Invert(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Levels(self, clip: "VideoNode", min_in: typing.Union[float, typing.Sequence[float], None] = None, max_in: typing.Union[float, typing.Sequence[float], None] = None, gamma: typing.Union[float, typing.Sequence[float], None] = None, min_out: typing.Union[float, typing.Sequence[float], None] = None, max_out: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Limiter(self, clip: "VideoNode", min: typing.Union[float, typing.Sequence[float], None] = None, max: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def LoadPlugin(self, path: typing.Union[str, bytes, bytearray], altsearchpath: typing.Optional[int] = None, forcens: typing.Union[str, bytes, bytearray, None] = None, forceid: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Loop(self, clip: "VideoNode", times: typing.Optional[int] = None) -> "VideoNode": ...
    def Lut(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, lut: typing.Union[int, typing.Sequence[int], None] = None, lutf: typing.Union[float, typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Optional[int] = None, floatout: typing.Optional[int] = None) -> "VideoNode": ...
    def Lut2(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, lut: typing.Union[int, typing.Sequence[int], None] = None, lutf: typing.Union[float, typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Optional[int] = None, floatout: typing.Optional[int] = None) -> "VideoNode": ...
    def MakeDiff(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MaskedMerge(self, clipa: "VideoNode", clipb: "VideoNode", mask: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, first_plane: typing.Optional[int] = None, premultiplied: typing.Optional[int] = None) -> "VideoNode": ...
    def Maximum(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None, coordinates: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Median(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Merge(self, clipa: "VideoNode", clipb: "VideoNode", weight: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def MergeDiff(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Minimum(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None, coordinates: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ModifyFrame(self, clip: "VideoNode", clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], selector: typing.Callable[..., typing.Any]) -> "VideoNode": ...
    def PEMVerifier(self, clip: "VideoNode", upper: typing.Union[float, typing.Sequence[float], None] = None, lower: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def PlaneStats(self, clipa: "VideoNode", clipb: typing.Optional["VideoNode"] = None, plane: typing.Optional[int] = None, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def PreMultiply(self, clip: "VideoNode", alpha: "VideoNode") -> "VideoNode": ...
    def Prewitt(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, scale: typing.Optional[float] = None) -> "VideoNode": ...
    def PropToClip(self, clip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Reverse(self, clip: "VideoNode") -> "VideoNode": ...
    def SelectEvery(self, clip: "VideoNode", cycle: int, offsets: typing.Union[int, typing.Sequence[int]], modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def SeparateFields(self, clip: "VideoNode", tff: typing.Optional[int] = None, modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def SetFieldBased(self, clip: "VideoNode", value: int) -> "VideoNode": ...
    def SetFrameProp(self, clip: "VideoNode", prop: typing.Union[str, bytes, bytearray], delete: typing.Optional[int] = None, intval: typing.Union[int, typing.Sequence[int], None] = None, floatval: typing.Union[float, typing.Sequence[float], None] = None, data: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None) -> "VideoNode": ...
    def SetMaxCPU(self, cpu: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def ShufflePlanes(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], planes: typing.Union[int, typing.Sequence[int]], colorfamily: int) -> "VideoNode": ...
    def Sobel(self, clip: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, scale: typing.Optional[float] = None) -> "VideoNode": ...
    def Splice(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], mismatch: typing.Optional[int] = None) -> "VideoNode": ...
    def StackHorizontal(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]]) -> "VideoNode": ...
    def StackVertical(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]]) -> "VideoNode": ...
    def Transpose(self, clip: "VideoNode") -> "VideoNode": ...
    def Trim(self, clip: "VideoNode", first: typing.Optional[int] = None, last: typing.Optional[int] = None, length: typing.Optional[int] = None) -> "VideoNode": ...
    def Turn180(self, clip: "VideoNode") -> "VideoNode": ...


class _Plugin_std_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AddBorders(self, left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None, color: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def AssumeFPS(self, src: typing.Optional["VideoNode"] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None) -> "VideoNode": ...
    def Binarize(self, threshold: typing.Union[float, typing.Sequence[float], None] = None, v0: typing.Union[float, typing.Sequence[float], None] = None, v1: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def BlankClip(self, width: typing.Optional[int] = None, height: typing.Optional[int] = None, format: typing.Optional[int] = None, length: typing.Optional[int] = None, fpsnum: typing.Optional[int] = None, fpsden: typing.Optional[int] = None, color: typing.Union[float, typing.Sequence[float], None] = None, keep: typing.Optional[int] = None) -> "VideoNode": ...
    def BoxBlur(self, planes: typing.Union[int, typing.Sequence[int], None] = None, hradius: typing.Optional[int] = None, hpasses: typing.Optional[int] = None, vradius: typing.Optional[int] = None, vpasses: typing.Optional[int] = None) -> "VideoNode": ...
    def Cache(self, size: typing.Optional[int] = None, fixed: typing.Optional[int] = None, make_linear: typing.Optional[int] = None) -> "VideoNode": ...
    def ClipToProp(self, mclip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Convolution(self, matrix: typing.Union[float, typing.Sequence[float]], bias: typing.Optional[float] = None, divisor: typing.Optional[float] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, saturate: typing.Optional[int] = None, mode: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Crop(self, left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None) -> "VideoNode": ...
    def CropAbs(self, width: int, height: int, left: typing.Optional[int] = None, top: typing.Optional[int] = None, x: typing.Optional[int] = None, y: typing.Optional[int] = None) -> "VideoNode": ...
    def CropRel(self, left: typing.Optional[int] = None, right: typing.Optional[int] = None, top: typing.Optional[int] = None, bottom: typing.Optional[int] = None) -> "VideoNode": ...
    def Deflate(self, planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None) -> "VideoNode": ...
    def DeleteFrames(self, frames: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def DoubleWeave(self, tff: typing.Optional[int] = None) -> "VideoNode": ...
    def DuplicateFrames(self, frames: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Expr(self, expr: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]]], format: typing.Optional[int] = None) -> "VideoNode": ...
    def FlipHorizontal(self) -> "VideoNode": ...
    def FlipVertical(self) -> "VideoNode": ...
    def FrameEval(self, eval: typing.Callable[..., typing.Any], prop_src: typing.Union["VideoNode", typing.Sequence["VideoNode"], None] = None) -> "VideoNode": ...
    def FreezeFrames(self, first: typing.Union[int, typing.Sequence[int]], last: typing.Union[int, typing.Sequence[int]], replacement: typing.Union[int, typing.Sequence[int]]) -> "VideoNode": ...
    def Inflate(self, planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None) -> "VideoNode": ...
    def Interleave(self, extend: typing.Optional[int] = None, mismatch: typing.Optional[int] = None, modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def Invert(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Levels(self, min_in: typing.Union[float, typing.Sequence[float], None] = None, max_in: typing.Union[float, typing.Sequence[float], None] = None, gamma: typing.Union[float, typing.Sequence[float], None] = None, min_out: typing.Union[float, typing.Sequence[float], None] = None, max_out: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Limiter(self, min: typing.Union[float, typing.Sequence[float], None] = None, max: typing.Union[float, typing.Sequence[float], None] = None, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def LoadPlugin(self, altsearchpath: typing.Optional[int] = None, forcens: typing.Union[str, bytes, bytearray, None] = None, forceid: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Loop(self, times: typing.Optional[int] = None) -> "VideoNode": ...
    def Lut(self, planes: typing.Union[int, typing.Sequence[int], None] = None, lut: typing.Union[int, typing.Sequence[int], None] = None, lutf: typing.Union[float, typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Optional[int] = None, floatout: typing.Optional[int] = None) -> "VideoNode": ...
    def Lut2(self, clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, lut: typing.Union[int, typing.Sequence[int], None] = None, lutf: typing.Union[float, typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Optional[int] = None, floatout: typing.Optional[int] = None) -> "VideoNode": ...
    def MakeDiff(self, clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MaskedMerge(self, clipb: "VideoNode", mask: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None, first_plane: typing.Optional[int] = None, premultiplied: typing.Optional[int] = None) -> "VideoNode": ...
    def Maximum(self, planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None, coordinates: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Median(self, planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Merge(self, clipb: "VideoNode", weight: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def MergeDiff(self, clipb: "VideoNode", planes: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Minimum(self, planes: typing.Union[int, typing.Sequence[int], None] = None, threshold: typing.Optional[float] = None, coordinates: typing.Union[int, typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ModifyFrame(self, clips: typing.Union["VideoNode", typing.Sequence["VideoNode"]], selector: typing.Callable[..., typing.Any]) -> "VideoNode": ...
    def PEMVerifier(self, upper: typing.Union[float, typing.Sequence[float], None] = None, lower: typing.Union[float, typing.Sequence[float], None] = None) -> "VideoNode": ...
    def PlaneStats(self, clipb: typing.Optional["VideoNode"] = None, plane: typing.Optional[int] = None, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def PreMultiply(self, alpha: "VideoNode") -> "VideoNode": ...
    def Prewitt(self, planes: typing.Union[int, typing.Sequence[int], None] = None, scale: typing.Optional[float] = None) -> "VideoNode": ...
    def PropToClip(self, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Reverse(self) -> "VideoNode": ...
    def SelectEvery(self, cycle: int, offsets: typing.Union[int, typing.Sequence[int]], modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def SeparateFields(self, tff: typing.Optional[int] = None, modify_duration: typing.Optional[int] = None) -> "VideoNode": ...
    def SetFieldBased(self, value: int) -> "VideoNode": ...
    def SetFrameProp(self, prop: typing.Union[str, bytes, bytearray], delete: typing.Optional[int] = None, intval: typing.Union[int, typing.Sequence[int], None] = None, floatval: typing.Union[float, typing.Sequence[float], None] = None, data: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None) -> "VideoNode": ...
    def SetMaxCPU(self) -> "VideoNode": ...
    def ShufflePlanes(self, planes: typing.Union[int, typing.Sequence[int]], colorfamily: int) -> "VideoNode": ...
    def Sobel(self, planes: typing.Union[int, typing.Sequence[int], None] = None, scale: typing.Optional[float] = None) -> "VideoNode": ...
    def Splice(self, mismatch: typing.Optional[int] = None) -> "VideoNode": ...
    def StackHorizontal(self) -> "VideoNode": ...
    def StackVertical(self) -> "VideoNode": ...
    def Transpose(self) -> "VideoNode": ...
    def Trim(self, first: typing.Optional[int] = None, last: typing.Optional[int] = None, length: typing.Optional[int] = None) -> "VideoNode": ...
    def Turn180(self) -> "VideoNode": ...
# end implementation


# implementation: tcanny
class _Plugin_tcanny_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TCanny(self, clip: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, sigma_v: typing.Union[typing.Sequence[float], None] = None, t_h: typing.Union[float, None] = None, t_l: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, op: typing.Union[int, None] = None, gmmax: typing.Union[float, None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def TCannyCL(self, clip: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, sigma_v: typing.Union[typing.Sequence[float], None] = None, t_h: typing.Union[float, None] = None, t_l: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, op: typing.Union[int, None] = None, gmmax: typing.Union[float, None] = None, device: typing.Union[int, None] = None, list_device: typing.Union[int, None] = None, info: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_tcanny_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TCanny(self, sigma: typing.Union[typing.Sequence[float], None] = None, sigma_v: typing.Union[typing.Sequence[float], None] = None, t_h: typing.Union[float, None] = None, t_l: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, op: typing.Union[int, None] = None, gmmax: typing.Union[float, None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def TCannyCL(self, sigma: typing.Union[typing.Sequence[float], None] = None, sigma_v: typing.Union[typing.Sequence[float], None] = None, t_h: typing.Union[float, None] = None, t_l: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, op: typing.Union[int, None] = None, gmmax: typing.Union[float, None] = None, device: typing.Union[int, None] = None, list_device: typing.Union[int, None] = None, info: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
# end implementation


# implementation: text
class _Plugin_text_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ClipInfo(self, clip: "VideoNode", alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def CoreInfo(self, clip: typing.Optional["VideoNode"] = None, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def FrameNum(self, clip: "VideoNode", alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def FrameProps(self, clip: "VideoNode", props: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def Text(self, clip: "VideoNode", text: typing.Union[str, bytes, bytearray], alignment: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_text_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ClipInfo(self, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def CoreInfo(self, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def FrameNum(self, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def FrameProps(self, props: typing.Union[str, bytes, bytearray, typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, alignment: typing.Optional[int] = None) -> "VideoNode": ...
    def Text(self, text: typing.Union[str, bytes, bytearray], alignment: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: tnlm
class _Plugin_tnlm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TNLMeans(self, clip: "VideoNode", ax: typing.Optional[int] = None, ay: typing.Optional[int] = None, az: typing.Optional[int] = None, sx: typing.Optional[int] = None, sy: typing.Optional[int] = None, bx: typing.Optional[int] = None, by: typing.Optional[int] = None, a: typing.Optional[float] = None, h: typing.Optional[float] = None, ssd: typing.Optional[int] = None) -> "VideoNode": ...


class _Plugin_tnlm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TNLMeans(self, ax: typing.Optional[int] = None, ay: typing.Optional[int] = None, az: typing.Optional[int] = None, sx: typing.Optional[int] = None, sy: typing.Optional[int] = None, bx: typing.Optional[int] = None, by: typing.Optional[int] = None, a: typing.Optional[float] = None, h: typing.Optional[float] = None, ssd: typing.Optional[int] = None) -> "VideoNode": ...
# end implementation


# implementation: vinverse
class _Plugin_vinverse_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Vinverse(self, clip: "VideoNode", sstr: typing.Optional[float] = None, amnt: typing.Optional[int] = None, scl: typing.Optional[float] = None) -> "VideoNode": ...


class _Plugin_vinverse_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Vinverse(self, sstr: typing.Optional[float] = None, amnt: typing.Optional[int] = None, scl: typing.Optional[float] = None) -> "VideoNode": ...
# end implementation


# implementation: vivtc
class _Plugin_vivtc_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VDecimate(self, clip: "VideoNode", cycle: typing.Optional[int] = None, chroma: typing.Optional[int] = None, dupthresh: typing.Optional[float] = None, scthresh: typing.Optional[float] = None, blockx: typing.Optional[int] = None, blocky: typing.Optional[int] = None, clip2: typing.Optional["VideoNode"] = None, ovr: typing.Union[str, bytes, bytearray, None] = None, dryrun: typing.Optional[int] = None) -> "VideoNode": ...
    def VFM(self, clip: "VideoNode", order: int, field: typing.Optional[int] = None, mode: typing.Optional[int] = None, mchroma: typing.Optional[int] = None, cthresh: typing.Optional[int] = None, mi: typing.Optional[int] = None, chroma: typing.Optional[int] = None, blockx: typing.Optional[int] = None, blocky: typing.Optional[int] = None, y0: typing.Optional[int] = None, y1: typing.Optional[int] = None, scthresh: typing.Optional[float] = None, micmatch: typing.Optional[int] = None, micout: typing.Optional[int] = None, clip2: typing.Optional["VideoNode"] = None) -> "VideoNode": ...


class _Plugin_vivtc_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VDecimate(self, cycle: typing.Optional[int] = None, chroma: typing.Optional[int] = None, dupthresh: typing.Optional[float] = None, scthresh: typing.Optional[float] = None, blockx: typing.Optional[int] = None, blocky: typing.Optional[int] = None, clip2: typing.Optional["VideoNode"] = None, ovr: typing.Union[str, bytes, bytearray, None] = None, dryrun: typing.Optional[int] = None) -> "VideoNode": ...
    def VFM(self, order: int, field: typing.Optional[int] = None, mode: typing.Optional[int] = None, mchroma: typing.Optional[int] = None, cthresh: typing.Optional[int] = None, mi: typing.Optional[int] = None, chroma: typing.Optional[int] = None, blockx: typing.Optional[int] = None, blocky: typing.Optional[int] = None, y0: typing.Optional[int] = None, y1: typing.Optional[int] = None, scthresh: typing.Optional[float] = None, micmatch: typing.Optional[int] = None, micout: typing.Optional[int] = None, clip2: typing.Optional["VideoNode"] = None) -> "VideoNode": ...
# end implementation


# implementation: znedi3
class _Plugin_znedi3_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, clip: "VideoNode", field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, nsize: typing.Optional[int] = None, nns: typing.Optional[int] = None, qual: typing.Optional[int] = None, etype: typing.Optional[int] = None, pscrn: typing.Optional[int] = None, opt: typing.Optional[int] = None, int16_prescreener: typing.Optional[int] = None, int16_predictor: typing.Optional[int] = None, exp: typing.Optional[int] = None, show_mask: typing.Optional[int] = None, x_nnedi3_weights_bin: typing.Union[str, bytes, bytearray, None] = None, x_cpu: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_znedi3_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, field: int, dh: typing.Optional[int] = None, planes: typing.Union[int, typing.Sequence[int], None] = None, nsize: typing.Optional[int] = None, nns: typing.Optional[int] = None, qual: typing.Optional[int] = None, etype: typing.Optional[int] = None, pscrn: typing.Optional[int] = None, opt: typing.Optional[int] = None, int16_prescreener: typing.Optional[int] = None, int16_predictor: typing.Optional[int] = None, exp: typing.Optional[int] = None, show_mask: typing.Optional[int] = None, x_nnedi3_weights_bin: typing.Union[str, bytes, bytearray, None] = None, x_cpu: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
# end implementation


class VideoNode:
# instance_bound: adg
    @property
    def adg(self) -> _Plugin_adg_Bound:
        """
        Adaptive grain
        """
# end instance
# instance_bound: bilateral
    @property
    def bilateral(self) -> _Plugin_bilateral_Bound:
        """
        Bilateral filter and Gaussian filter for VapourSynth.
        """
# end instance
# instance_bound: bm3d
    @property
    def bm3d(self) -> _Plugin_bm3d_Bound:
        """
        Implementation of BM3D denoising filter for VapourSynth.
        """
# end instance
# instance_bound: comb
    @property
    def comb(self) -> _Plugin_comb_Bound:
        """
        comb filters v0.0.1
        """
# end instance
# instance_bound: d2v
    @property
    def d2v(self) -> _Plugin_d2v_Bound:
        """
        D2V Source
        """
# end instance
# instance_bound: descale
    @property
    def descale(self) -> _Plugin_descale_Bound:
        """
        Undo linear interpolation
        """
# end instance
# instance_bound: dfttest
    @property
    def dfttest(self) -> _Plugin_dfttest_Bound:
        """
        2D/3D frequency domain denoiser
        """
# end instance
# instance_bound: dgdecodenv
    @property
    def dgdecodenv(self) -> _Plugin_dgdecodenv_Bound:
        """
        dgdecnv quick stubs
        """
# end instance
# instance_bound: edgefixer
    @property
    def edgefixer(self) -> _Plugin_edgefixer_Bound:
        """
        VapourSynth edgefixer port
        """
# end instance
# instance_bound: eedi3m
    @property
    def eedi3m(self) -> _Plugin_eedi3m_Bound:
        """
        Enhanced Edge Directed Interpolation 3
        """
# end instance
# instance_bound: ffms2
    @property
    def ffms2(self) -> _Plugin_ffms2_Bound:
        """
        FFmpegSource 2 for VapourSynth
        """
# end instance
# instance_bound: fmtc
    @property
    def fmtc(self) -> _Plugin_fmtc_Bound:
        """
        Format converter, r22
        """
# end instance
# instance_bound: imwri
    @property
    def imwri(self) -> _Plugin_imwri_Bound:
        """
        VapourSynth ImageMagick 7 HDRI Writer/Reader
        """
# end instance
# instance_bound: knlm
    @property
    def knlm(self) -> _Plugin_knlm_Bound:
        """
        KNLMeansCL for VapourSynth
        """
# end instance
# instance_bound: lsmas
    @property
    def lsmas(self) -> _Plugin_lsmas_Bound:
        """
        LSMASHSource for VapourSynth
        """
# end instance
# instance_bound: mpls
    @property
    def mpls(self) -> _Plugin_mpls_Bound:
        """
        Get m2ts clip id from a playlist and return a dict
        """
# end instance
# instance_bound: nnedi3
    @property
    def nnedi3(self) -> _Plugin_nnedi3_Bound:
        """
        Neural network edge directed interpolation (3rd gen.), v12
        """
# end instance
# instance_bound: nnedi3cl
    @property
    def nnedi3cl(self) -> _Plugin_nnedi3cl_Bound:
        """
        An intra-field only deinterlacer
        """
# end instance
# instance_bound: resize
    @property
    def resize(self) -> _Plugin_resize_Bound:
        """
        VapourSynth Resize
        """
# end instance
# instance_bound: retinex
    @property
    def retinex(self) -> _Plugin_retinex_Bound:
        """
        Implementation of Retinex algorithm for VapourSynth.
        """
# end instance
# instance_bound: rgsf
    @property
    def rgsf(self) -> _Plugin_rgsf_Bound:
        """
        RemoveGrain Single Precision
        """
# end instance
# instance_bound: rgvs
    @property
    def rgvs(self) -> _Plugin_rgvs_Bound:
        """
        RemoveGrain VapourSynth Port
        """
# end instance
# instance_bound: std
    @property
    def std(self) -> _Plugin_std_Bound:
        """
        VapourSynth Core Functions
        """
# end instance
# instance_bound: tcanny
    @property
    def tcanny(self) -> _Plugin_tcanny_Bound:
        """
        Build an edge map using canny edge detection
        """
# end instance
# instance_bound: text
    @property
    def text(self) -> _Plugin_text_Bound:
        """
        VapourSynth Text
        """
# end instance
# instance_bound: tnlm
    @property
    def tnlm(self) -> _Plugin_tnlm_Bound:
        """
        TNLMeans rev-
        """
# end instance
# instance_bound: vinverse
    @property
    def vinverse(self) -> _Plugin_vinverse_Bound:
        """
        A simple filter to remove residual combing.
        """
# end instance
# instance_bound: vivtc
    @property
    def vivtc(self) -> _Plugin_vivtc_Bound:
        """
        VFM
        """
# end instance
# instance_bound: znedi3
    @property
    def znedi3(self) -> _Plugin_znedi3_Bound:
        """
        Neural network edge directed interpolation (3rd gen.)
        """
# end instance

    format: typing.Optional[Format]

    fps: fractions.Fraction
    fps_den: int
    fps_num: int

    height: int
    width: int

    num_frames: int
    flags: int

    def get_frame(self, n: int) -> VideoFrame: ...
    def get_frame_async_raw(self, n: int, cb: _Future[VideoFrame], future_wrapper: typing.Optional[typing.Callable[..., None]]=None) -> _Future[VideoFrame]: ...
    def get_frame_async(self, n: int) -> _Future[VideoFrame]: ...

    def set_output(self, index: int=0, alpha: typing.Optional['VideoNode']=None) -> None: ...
    def output(self, fileobj: typing.BinaryIO, y4m: bool = False, progress_update: typing.Optional[typing.Callable[[int], int]]=None, prefetch: int = 0) -> None: ...

    def frames(self) -> typing.Iterator[VideoFrame]: ...

    def __add__(self, other: 'VideoNode') -> 'VideoNode': ...
    def __mul__(self, other: int) -> 'VideoNode': ...
    def __getitem__(self, other: typing.Union[int, slice]) -> 'VideoNode': ...
    def __len__(self) -> int: ...


class _PluginMeta(typing.TypedDict):
    namespace: str
    identifier: str
    name: str
    functions: typing.Dict[str, str]


class Core:
# instance_unbound: adg
    @property
    def adg(self) -> _Plugin_adg_Unbound:
        """
        Adaptive grain
        """
# end instance
# instance_unbound: bilateral
    @property
    def bilateral(self) -> _Plugin_bilateral_Unbound:
        """
        Bilateral filter and Gaussian filter for VapourSynth.
        """
# end instance
# instance_unbound: bm3d
    @property
    def bm3d(self) -> _Plugin_bm3d_Unbound:
        """
        Implementation of BM3D denoising filter for VapourSynth.
        """
# end instance
# instance_unbound: comb
    @property
    def comb(self) -> _Plugin_comb_Unbound:
        """
        comb filters v0.0.1
        """
# end instance
# instance_unbound: d2v
    @property
    def d2v(self) -> _Plugin_d2v_Unbound:
        """
        D2V Source
        """
# end instance
# instance_unbound: descale
    @property
    def descale(self) -> _Plugin_descale_Unbound:
        """
        Undo linear interpolation
        """
# end instance
# instance_unbound: dfttest
    @property
    def dfttest(self) -> _Plugin_dfttest_Unbound:
        """
        2D/3D frequency domain denoiser
        """
# end instance
# instance_unbound: dgdecodenv
    @property
    def dgdecodenv(self) -> _Plugin_dgdecodenv_Unbound:
        """
        dgdecnv quick stubs
        """
# end instance
# instance_unbound: edgefixer
    @property
    def edgefixer(self) -> _Plugin_edgefixer_Unbound:
        """
        VapourSynth edgefixer port
        """
# end instance
# instance_unbound: eedi3m
    @property
    def eedi3m(self) -> _Plugin_eedi3m_Unbound:
        """
        Enhanced Edge Directed Interpolation 3
        """
# end instance
# instance_unbound: ffms2
    @property
    def ffms2(self) -> _Plugin_ffms2_Unbound:
        """
        FFmpegSource 2 for VapourSynth
        """
# end instance
# instance_unbound: fmtc
    @property
    def fmtc(self) -> _Plugin_fmtc_Unbound:
        """
        Format converter, r22
        """
# end instance
# instance_unbound: imwri
    @property
    def imwri(self) -> _Plugin_imwri_Unbound:
        """
        VapourSynth ImageMagick 7 HDRI Writer/Reader
        """
# end instance
# instance_unbound: knlm
    @property
    def knlm(self) -> _Plugin_knlm_Unbound:
        """
        KNLMeansCL for VapourSynth
        """
# end instance
# instance_unbound: lsmas
    @property
    def lsmas(self) -> _Plugin_lsmas_Unbound:
        """
        LSMASHSource for VapourSynth
        """
# end instance
# instance_unbound: mpls
    @property
    def mpls(self) -> _Plugin_mpls_Unbound:
        """
        Get m2ts clip id from a playlist and return a dict
        """
# end instance
# instance_unbound: nnedi3
    @property
    def nnedi3(self) -> _Plugin_nnedi3_Unbound:
        """
        Neural network edge directed interpolation (3rd gen.), v12
        """
# end instance
# instance_unbound: nnedi3cl
    @property
    def nnedi3cl(self) -> _Plugin_nnedi3cl_Unbound:
        """
        An intra-field only deinterlacer
        """
# end instance
# instance_unbound: resize
    @property
    def resize(self) -> _Plugin_resize_Unbound:
        """
        VapourSynth Resize
        """
# end instance
# instance_unbound: retinex
    @property
    def retinex(self) -> _Plugin_retinex_Unbound:
        """
        Implementation of Retinex algorithm for VapourSynth.
        """
# end instance
# instance_unbound: rgsf
    @property
    def rgsf(self) -> _Plugin_rgsf_Unbound:
        """
        RemoveGrain Single Precision
        """
# end instance
# instance_unbound: rgvs
    @property
    def rgvs(self) -> _Plugin_rgvs_Unbound:
        """
        RemoveGrain VapourSynth Port
        """
# end instance
# instance_unbound: std
    @property
    def std(self) -> _Plugin_std_Unbound:
        """
        VapourSynth Core Functions
        """
# end instance
# instance_unbound: tcanny
    @property
    def tcanny(self) -> _Plugin_tcanny_Unbound:
        """
        Build an edge map using canny edge detection
        """
# end instance
# instance_unbound: text
    @property
    def text(self) -> _Plugin_text_Unbound:
        """
        VapourSynth Text
        """
# end instance
# instance_unbound: tnlm
    @property
    def tnlm(self) -> _Plugin_tnlm_Unbound:
        """
        TNLMeans rev-
        """
# end instance
# instance_unbound: vinverse
    @property
    def vinverse(self) -> _Plugin_vinverse_Unbound:
        """
        A simple filter to remove residual combing.
        """
# end instance
# instance_unbound: vivtc
    @property
    def vivtc(self) -> _Plugin_vivtc_Unbound:
        """
        VFM
        """
# end instance
# instance_unbound: znedi3
    @property
    def znedi3(self) -> _Plugin_znedi3_Unbound:
        """
        Neural network edge directed interpolation (3rd gen.)
        """
# end instance

    num_threads: int
    max_cache_size: int
    add_cache: bool

    def set_max_cache_size(self, mb: int) -> int: ...
    def get_plugins(self) -> typing.Dict[str, _PluginMeta]: ...
    def list_functions(self) -> str: ...

    def register_format(self, color_family: ColorFamily, sample_type: SampleType, bits_per_sample: int, subsampling_w: int, subsampling_h: int) -> Format: ...
    def get_format(self, id: typing.Union[Format, int, PresetFormat]) -> Format: ...

    def version(self) -> str: ...
    def version_number(self) -> int: ...


def get_core(threads: typing.Optional[int]=None, add_cache: typing.Optional[bool]=None) -> Core: ...


class _CoreProxy(Core):
    core: Core


core: _CoreProxy
