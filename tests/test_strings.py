import pytest

from textkit import reverse, slugify, word_count


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


def test_word_count_nhieu_tu():
    assert word_count("Xin chào Việt Nam") == 4


def test_word_count_mot_tu():
    assert word_count("Xin") == 1


def test_word_count_chuoi_rong():
    assert word_count("") == 0


def test_word_count_chuoi_chi_co_khoang_trang():
    assert word_count("   \t  ") == 0


def test_word_count_none_thi_nem():
    with pytest.raises(ValueError):
        word_count(None)
