#!/usr/bin/python3
"""
Define class Rec.
"""


class Rectangle:
    """
    Represent a rec.

    Args:
        width: the width of rec.
        height: th height.

    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rec.

        Args:
            width: width of rec.
            height: height of rec.

        Returns:
            None

        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Get the width.

        Returns:
            int: width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set new val."""
        if type(value) is not int or type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if value < 0 or self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height.

        Retruns:
            int: the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set new val."""
        if type(value) is not int or type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if value < 0 or self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
