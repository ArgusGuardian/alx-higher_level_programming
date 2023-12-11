#!/usr/bin/python3
"""Module for the Square class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class in the sqaure module"""

    def __init__(self, size, x=0, y=0, id=None):
        """function to initialize the Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter function fo size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter function for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Funtion that updates the arguments"""
        if args and len(args) != 0:
            self.__init__(self.size, self.x, self.y)
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """return dict of all atrributes"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """Retrun the str() representation of the Square class"""
        return f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.size}"
