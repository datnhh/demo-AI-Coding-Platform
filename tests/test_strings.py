import pytest

from textkit import reverse, slugify, visible_length


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


def test_visible_length_chuoi_thuong():
    assert visible_length("abc def") == 6


def test_visible_length_chuoi_rong():
    assert visible_length("") == 0


def test_visible_length_toan_khoang_trang():
    assert visible_length("   \t\n  ") == 0


def test_visible_length_khoang_trang_hon_hop():
    assert visible_length("  a b\tc\n") == 3


def test_visible_length_none_thi_nem():
    with pytest.raises(ValueError):
        visible_length(None)
