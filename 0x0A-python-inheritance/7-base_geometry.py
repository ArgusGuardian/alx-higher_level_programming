#!/usr/bin/python3
"""dfines an empty class"""


class BaseGeometry:
    """this is an empty class"""

    def area(self):
        """useless area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """functiom to validate the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
