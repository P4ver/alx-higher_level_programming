#!/usr/bin/python3
"""Lookup methode,"""


def lookup(obj):
    """
    Args:
        obj: could be anyting (object).
    Returns:
        returns a list of available attributes and methods of an obj.
    """
    return dir(obj)
