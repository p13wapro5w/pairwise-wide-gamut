import pytest
from color import wide_gamut as mod

CASES = [
    ("srgb_black", 'm.srgb_to_linear(0.0) == approx(0.0)'),
    ("srgb_white", 'm.srgb_to_linear(1.0) == approx(1.0)'),
    ("srgb_mid", 'm.srgb_to_linear(0.5) == approx(0.2140, rel=1e-3)'),
    ("p3_red", 'm.p3_to_srgb((1.0, 0.0, 0.0)) == approx((0.95, 0.0, 0.0))'),
    ("hue_wrap", 'm.hue_shift(350.0, 20.0) == approx(10.0)'),
    ("hue_plain", 'm.hue_shift(10.0, 20.0) == approx(30.0)'),
    ("lut_index", 'm.lut3d_index(1, 2, 3, 4) == 27'),
    ("lut_zero", 'm.lut3d_index(0, 0, 0, 4) == 0'),
    ("exposure", 'm.exposure_once(1.0, 1.0) == approx(2.0)'),
    ("blend_mid", 'm.linear_blend(0.0, 1.0, 0.5) == approx(0.5)'),
    ("encode_sdr", 'm.output_encode(2.0, False) == approx(1.0)'),
    ("encode_hdr", 'm.output_encode(2.0, True) == approx(2.0)'),
    ("gamma_console", 'm.gamma_for_platform("console") == approx(2.4)'),
    ("grade_lut", 'm.grade_order("lut") == 1'),
    ("bucket_p3", 'm.colorspace_bucket("P3") == "p3"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
