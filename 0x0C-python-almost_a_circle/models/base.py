#!usr/bin/python3
"""base module."""


class Base:
    """Representing base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
