#!/usr/bin/python3
"""rect module."""

from models.base import Base


class Rectangle(Base):
    """representing the rectangle that is inherit."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inisializing"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter _val of width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter new_val of width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter _val of height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter _val of x"""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter _val of y"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """clac the area ofrect."""
        return self.__width * self.__height

    def display(self):
        """displaying #hash."""
        for g in range(self.__y):
            print()
        for u in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """representing rect."""
        return f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.__width = args[1]
        if len(args) == 3:
            self.__height = args[2]
        if len(args) == 4:
            self.__x = args[3]
        if len(args) == 5:
            self.__y = args[4]
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.__width = kwargs['width']
        if 'height' in kwargs:
            self.__height = kwargs['height']
        if 'x' in kwargs:
            self.__x = kwargs['x']
        if 'y' in kwargs:
            self.__y = kwargs['y']
