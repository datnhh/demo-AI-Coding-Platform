import pytest

from textkit import repeat, reverse, slugify


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


def test_repeat_chuoi_thuong():
    assert repeat("ab", 3) == "ababab"


def test_repeat_times_bang_0():
    assert repeat("ab", 0) == ""


def test_repeat_chuoi_rong():
    assert repeat("", 5) == ""


def test_repeat_none_thi_nem():
    with pytest.raises(ValueError):
        repeat(None, 3)


def test_repeat_times_am_thi_nem():
    with pytest.raises(ValueError):
        repeat("ab", -1)
