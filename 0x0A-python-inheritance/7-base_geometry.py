#!/usr/bin/python3
"""dfines an empty class"""


class BaseGeometry:
    """this is an empty class"""

    def area(self):
        """useless area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """functiom to validate the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
