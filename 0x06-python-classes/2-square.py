#!/usr/bin/python3
"""modl of  class square."""


class Square:
    """Representing class square."""

    def __init__(self, size=0):
        """Initializing new instance.

        Args:
            size: size of sqr.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
