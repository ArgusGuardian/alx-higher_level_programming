#!/usr/bin/python3
"""Defines a function to add two integers or floats"""


def add_integer(a, b=98):
    """Add two integers or floats

    Args:
        a: The first number
        b: The second number (default is 98)

    Raises:
        TypeError: If a is not an int or float
        TypeError: If b is not an int or float

    Returns:
        The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
