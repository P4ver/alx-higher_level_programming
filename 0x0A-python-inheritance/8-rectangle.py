#!/usr/bin/python3
"""geo module,"""


class BaseGeometry:
    """geo class."""
    def area(self):
        """display exceptation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """funct that validate vlue."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class rectangle ,"""
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
