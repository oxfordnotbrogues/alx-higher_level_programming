#!/usr/bin/python3
"""Create a Rectangle class."""


class Rectangle:
    """Definition of a clas rectangle."""

    def __init__(self, width=0, height=0):
        """initializing Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
