#!/usr/bin/python3
"""Class square mdl."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, vlr):
        if type(vlr) != int:
            raise TypeError("size must be an integer")
        if vlr < 0:
            raise ValueError("size must be >= 0")
        self.__size = vlr

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, vlr):
        if type(vlr) != tuple or len(vlr) !=2 or not all(type(q) != int and q >= 0 for q in vlr):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = vlr

    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size != 0:
            for q in range(self.__position[1]):
                print()
            for q in range(self.__size):
                print(" " * self.__postion[0] + "#" * self.__size)
