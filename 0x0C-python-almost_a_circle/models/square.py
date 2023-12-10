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
        """get size of 'sqr'."""
        return self.width

    @size.setter
    def size(self, val):
        """set the size of 'sqr'."""
        self.width = val
        self.height = val

    def __str__(self):
        """str representation for sqr."""
        return f"[{type(self).__name__}] ({self.id}) {super().x}/{super().y} - {self.width}"
