#!/usr/bin/python3
"""Class square mdl."""


class Square:
    """Representing class square."""

    def __init__(self, size=0):
        """Initializing new instance.

        Args:
            size: size of sqr.
        """
        self.__size = size

    @property
    def size(self):
        """Getter methode for size attr.

        Returns:
            the size square
        """
        return self.__size

    @size.setter
    def size(self, vlr):
        """Setter method for size attr.

        Args:
            vlr: the new size.
        """
        if type(vlr) != int:
            raise TypeError("size must be an integer")
        if vlr < 0:
            raise ValueError("size must be >= 0")
        self.__size = vlr

    def area(self):
        """calc square's area.

        Returns:
            The area vlr
        """
        return self.__size * self.__size

    def my_print(self):
        """method printd in stdout the square '#'"""

        if self.__size != 0:
            for q in range(self.__size):
                print("#" * self.__size)
        else:
            print()
