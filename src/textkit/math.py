"""Cac ham toan hoc co ban."""

import math


def factorial(n: int) -> int:
    """Tinh giai thua cua mot so nguyen khong am n.

    Args:
        n: So nguyen khong am can tinh giai thua.

    Returns:
        Giai thua cua n (n!).

    Raises:
        ValueError: Neu n la None hoac n < 0.
        TypeError: Neu n khong phai so nguyen.
    """
    if n is None:
        raise ValueError("n khong duoc None")
    if not isinstance(n, int):
        raise TypeError("n phai la so nguyen")
    if n < 0:
        raise ValueError("n phai la so nguyen khong am")

    return math.factorial(n)
