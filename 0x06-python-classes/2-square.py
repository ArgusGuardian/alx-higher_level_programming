#!/usr/bin/python3
"""this file will have a more advanced square class"""


class Square:
    """this is the square class"""
    def __init__(self, size=0) -> None:
        """init function for the class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
