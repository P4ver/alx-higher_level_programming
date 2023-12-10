#!/usr/bin/python3
"""Module of sqr."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """representing 'sqr' class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        self.__size = val

    def __str__(self):
        return f"[Square] ({self.id}) {super().x}/{super().y} - {self.__size}"
