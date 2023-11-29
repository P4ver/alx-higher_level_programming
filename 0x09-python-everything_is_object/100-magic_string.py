#!/usr/bin/python3
"""Module 100-magic_string. """


def magic_string(counter=[0]):
    """
    Returns:
        str: prints str n times.
    """
    counter[0] += 1
    return "BestSchool" + ", BestSchool" * (counter[0] - 1)
