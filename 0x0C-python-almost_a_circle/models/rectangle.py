#!/usr/bin/python3
"""Rectangle Module"""
from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function for the Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter function for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for the width"""
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter function for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter function for the height"""

        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for the x"""
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function for the y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter function for the y"""

        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Funtion to calculate the rect area"""
        return self.__width * self.__height

    def display(self):
        """function that prints the rectangle"""
        for j in range(self.y):
            print()

        for i in range(self.__height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Funtion that updates the arguments"""
        self.__init__(self.width, self.height, self.x, self.y)
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    self.id = b
                elif a == "width":
                    self.width = b
                elif a == "height":
                    self.height = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """Retrun the str() representation of the Rect class"""
        return f"[Rectangle] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}"
