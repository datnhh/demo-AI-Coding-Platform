import pytest

from textkit import reverse, slugify, strip_prefix


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


def test_strip_prefix_co_tien_to():
    assert strip_prefix("hello_world", "hello_") == "world"


def test_strip_prefix_khong_co_tien_to():
    assert strip_prefix("hello_world", "xin_") == "hello_world"


def test_strip_prefix_chuoi_rong():
    assert strip_prefix("", "abc") == ""


def test_strip_prefix_tien_to_rong():
    assert strip_prefix("hello", "") == "hello"


def test_strip_prefix_tien_to_dai_hon_chuoi():
    assert strip_prefix("ab", "abcd") == "ab"


def test_strip_prefix_value_none_thi_nem():
    with pytest.raises(ValueError):
        strip_prefix(None, "abc")


def test_strip_prefix_prefix_none_thi_nem():
    with pytest.raises(ValueError):
        strip_prefix("abc", None)
