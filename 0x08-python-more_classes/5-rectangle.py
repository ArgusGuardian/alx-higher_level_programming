#!/usr/bin/python3
"""This is the Rectangle class."""


class Rectangle:
    """This is the Rectangle class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return (self.height * self.width)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if not self.height or not self.width:
            return 0
        return (2*(self.height+self.width))

    def __str__(self):
        """Return a string  of the rectangle using '#' characters."""
        if not self.width or not self.height:
            return ""
        double = ""
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                row += "#"
            double += row + '\n'
        return double

    def __repr__(self) -> str:
        """Return a string representation of the rectangle for debugging."""
        return f"Rectangle({self.width},{self.height})"

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
