import pytest

from textkit import reverse, slugify, truncate


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


def test_truncate_chuoi_ngan_hon_limit_giu_nguyen():
    assert truncate("abc", 5) == "abc"


def test_truncate_chuoi_bang_limit_giu_nguyen():
    assert truncate("abcde", 5) == "abcde"


def test_truncate_chuoi_dai_hon_limit_them_ba_cham():
    assert truncate("abcdef", 5) == "abcde..."


def test_truncate_none_thi_nem():
    with pytest.raises(ValueError):
        truncate(None, 5)


def test_truncate_limit_nho_hon_1_thi_nem():
    with pytest.raises(ValueError):
        truncate("abc", 0)
