#!/usr/bin/python3
"""Module 0-add_integer,"""


def add_integer(a, b=98):
    """
    Add two nm_b.

    Args:
        a: frst num,
        b: secnd num,

    Returns:
        int: the sum a + b,

    Raises:
        TypeError: if they are not int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
