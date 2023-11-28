#!/usr/bin/python3
"""Define class rec."""


class Rectangle:
    """Represent of rec."""
    def __init__(self, width=0, height=0):
        """Initialize the rec."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get i_a the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Calc the_area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calc _permtr."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns and display the rec as '#'."""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return '\n'.join(
                    ["#" * self.__width for q in range(self.__height)]
            )
