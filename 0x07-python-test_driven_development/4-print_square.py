#!/usr/bin/python3
"""Module 4-print_square"""


def print_square(size):
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    for q in range(size):
        print("#" * size)


if __name__ == '__main__':
    import doctest
    doctest.testfile(tests/4-print_square.txt)
