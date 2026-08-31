import pytest

from textkit import reverse, slugify, squeeze_spaces


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


def test_squeeze_spaces_gop_khoang_trang_lien_tiep():
    assert squeeze_spaces("a   b\t\tc") == "a b c"


def test_squeeze_spaces_cat_hai_dau():
    assert squeeze_spaces("  a b  ") == "a b"


def test_squeeze_spaces_xuong_dong():
    assert squeeze_spaces("a\n\nb") == "a b"


def test_squeeze_spaces_chuoi_rong():
    assert squeeze_spaces("") == ""


def test_squeeze_spaces_chi_co_khoang_trang():
    assert squeeze_spaces("   ") == ""


def test_squeeze_spaces_none_thi_nem():
    with pytest.raises(ValueError):
        squeeze_spaces(None)
