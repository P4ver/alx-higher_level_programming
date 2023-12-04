#!/usr/bin/python3
"""geo module,"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square."""
    def __init__(self, size):
        """
        Initialize instanc,

        Args:
            size: the size of squre.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """"method to calc area."""
        return self.__size ** 2

    def __str__(self):
        """return strng  repsentation of square."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
