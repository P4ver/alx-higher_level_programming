#!/usr/bin/python3
"""Module 5-text_indentation."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of .  ? and ':'.

    Args:
        text: string.
    Raises:
        TypeError: if not str.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    cr_c = ""
    mrk_sym = {'?', '.', ':'}
    for q in text:
        cr_c += q
        if q in mrk_sym:
            print(cr_c.strip())
            print()
            cr_c = ""

    if cr_c:
        print(cr_c.strip(), end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
