import pytest

from textkit import reverse, slugify


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
