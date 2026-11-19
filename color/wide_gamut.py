"""第 57 批：同一张 HDR 贴图在编辑器里正常，进游戏后高光..."""

def srgb_to_linear(value):
    """把 sRGB 分量转到线性。"""
    raise NotImplementedError("TODO: srgb_to_linear")

def p3_to_srgb(rgb):
    """把 Display-P3 转到 sRGB 范围。"""
    raise NotImplementedError("TODO: p3_to_srgb")

def hue_shift(hue, delta):
    """按角度移动色相。"""
    raise NotImplementedError("TODO: hue_shift")

def lut3d_index(r, g, b, size):
    """返回 3D LUT 线性索引。"""
    raise NotImplementedError("TODO: lut3d_index")

def exposure_once(value, ev):
    """只做一次曝光补偿。"""
    raise NotImplementedError("TODO: exposure_once")

def linear_blend(a, b, t):
    """在线性空间混合。"""
    raise NotImplementedError("TODO: linear_blend")

def output_encode(value, is_hdr):
    """按输出目标编码。"""
    raise NotImplementedError("TODO: output_encode")

def gamma_for_platform(platform):
    """返回平台 gamma。"""
    raise NotImplementedError("TODO: gamma_for_platform")

def grade_order(name):
    """返回分级节点顺序。"""
    raise NotImplementedError("TODO: grade_order")

def colorspace_bucket(colorspace):
    """返回色彩空间分组键。"""
    raise NotImplementedError("TODO: colorspace_bucket")
