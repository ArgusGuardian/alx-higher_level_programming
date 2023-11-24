#!/usr/bin/python3
"""Function that prints a square base on the var size"""


def print_square(size):
    """Print a square made of '#' characters

    Args:
        size: The size of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
