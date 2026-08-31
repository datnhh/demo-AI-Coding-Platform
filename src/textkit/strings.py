"""Vài hàm xử lý chuỗi, cố tình để mỏng cho agent có chỗ thêm việc."""

import re
import unicodedata


def reverse(value: str) -> str:
    """Đảo ngược một chuỗi."""
    if value is None:
        raise ValueError("value khong duoc None")

    return value[::-1]


def slugify(value: str) -> str:
    """Đưa chuỗi về dạng slug dùng được trong URL."""
    if value is None:
        raise ValueError("value khong duoc None")

    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")

    return re.sub(r"[^a-z0-9]+", "-", ascii_only.lower()).strip("-")


def repeat(value: str, times: int) -> str:
    """Lặp lại chuỗi value times lần."""
    if value is None:
        raise ValueError("value khong duoc None")
    if times < 0:
        raise ValueError("times khong duoc nho hon 0")

    return value * times
