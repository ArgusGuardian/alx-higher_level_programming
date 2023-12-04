#!/usr/bin/python3
"""defines a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class tha inherantes frmo basegeometry"""

    def __init__(self, width, height):
        """ initialize the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
