#!/usr/bin/python3
"""this file will have a more advanced square class"""


class Square:
    """this is the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init function for the class square"""
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """retrieve or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size:
            [print() for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print()
        else:
            print()

    @property
    def position(self):
        """retrieve or set the size of the position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Print the square with the # character."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print()
        return ("")
