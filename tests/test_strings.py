import pytest

from textkit import reverse, slugify, title_case


def test_reverse_chuoi_thuong():
    assert reverse("abc") == "cba"


def test_reverse_chuoi_rong():
    assert reverse("") == ""


def test_reverse_none_thi_nem():
    with pytest.raises(ValueError):
        reverse(None)


def test_slugify_bo_dau_tieng_viet():
    assert slugify("Xin chào Việt Nam") == "xin-chao-viet-nam"


def test_slugify_gop_ky_tu_la():
    assert slugify("A  --  B!!") == "a-b"


def test_title_case_chuoi_thuong():
    assert title_case("xin chao viet nam") == "Xin Chao Viet Nam"


def test_title_case_chu_hoa_lan():
    assert title_case("XIN chào VIỆT nam") == "Xin Chào Việt Nam"


def test_title_case_giu_nguyen_khoang_trang():
    assert title_case("xin   chao\tviet nam") == "Xin   Chao\tViet Nam"


def test_title_case_chuoi_rong():
    assert title_case("") == ""


def test_title_case_khoang_trang_dau_cuoi():
    assert title_case("  xin chao  ") == "  Xin Chao  "


def test_title_case_none_thi_nem():
    with pytest.raises(ValueError):
        title_case(None)
