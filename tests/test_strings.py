import pytest

from textkit import reverse, slugify, strip_suffix


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


def test_strip_suffix_co_hau_to():
    assert strip_suffix("hello.py", ".py") == "hello"


def test_strip_suffix_khong_co_hau_to():
    assert strip_suffix("hello.py", ".txt") == "hello.py"


def test_strip_suffix_hau_to_rong():
    assert strip_suffix("hello", "") == "hello"


def test_strip_suffix_chuoi_rong():
    assert strip_suffix("", "abc") == ""


def test_strip_suffix_trung_khop_toan_bo():
    assert strip_suffix("abc", "abc") == ""


def test_strip_suffix_value_none_thi_nem():
    with pytest.raises(ValueError):
        strip_suffix(None, ".py")


def test_strip_suffix_suffix_none_thi_nem():
    with pytest.raises(ValueError):
        strip_suffix("hello.py", None)
