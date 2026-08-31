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


def title_case(value: str) -> str:
    """Viết hoa chữ cái đầu mỗi từ, các chữ còn lại viết thường."""
    if value is None:
        raise ValueError("value khong duoc None")

    parts = re.split(r"(\s+)", value)
    return "".join(
        part if part.isspace() else part[:1].upper() + part[1:].lower()
        for part in parts
    )
