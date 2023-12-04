#!/usr/bin/python3
"""defines a squate class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square classs inhereanted from rectangle"""

    def __init__(self, size):
        """initialize the sqaure class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return the surface of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
