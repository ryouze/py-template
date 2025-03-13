"""
Module: foo.py

Example module.
"""

from random import randint as _randint

__all__: list[str] = [
    "bar",
    "baz",
]


def bar() -> int:
    """
    Return 0.

    Returns:
        int: 0.
    """
    return 0


def baz(
    size: int = 10,
) -> list[int]:
    """
    Return a list of random integers between 0 and 100 of the given size.

    Args:
        size (int, optional): Length of the list to return. Defaults to 10.

    Returns:
        list[int]: List of random integers.
    """
    return [_randint(0, 100) for _ in range(size)]
