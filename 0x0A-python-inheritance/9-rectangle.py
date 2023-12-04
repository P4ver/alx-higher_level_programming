#!/usr/bin/python3
"""geo module,"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle."""
    def __init__(self, width, height):
        """
        Initialize instanc,

        Args:
            width: rectang width.
            height: rec height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """"method to calc area."""
        return self.__width * self.__height

    def __str__(self):
        """return strng  repsentation of rec."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
