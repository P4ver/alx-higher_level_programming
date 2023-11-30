#!/usr/bin/python3
"""Module say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: string frst name.
        last_name: string lst nmae.
    Raises:
        TypeError: if it is not str.
    """
    if not(type(first_name) is str):
        raise TypeError("first_name must be a string")
    if not(type(last_name) is str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
