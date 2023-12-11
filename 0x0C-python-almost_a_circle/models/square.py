#!/usr/bin/python3
"""Module of sqr."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """representing 'sqr' class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing."""
        super().__init__(size, size, x, y, id)

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
        return f"[{type(self).__name__}] ({self.id}) "\
            f"{super().x}/{super().y} - {self.width}"

    def update(self, *args, **kwargs):
        """update the val of sqr either *arg or **kwarg."""
        if args:
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
            else:
                self.id = args[0]
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """return dict of 'sqr'."""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
