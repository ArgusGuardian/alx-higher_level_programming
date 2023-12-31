#!/usr/bin/python3
"""A function prints name and last name"""


def say_my_name(first_name, last_name=""):
    """Print a formatted name based on first_name and last_name

    Args:
        first_name: The first name
        last_name: The last name (default is an empty string)

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
