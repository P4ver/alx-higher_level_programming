#!/usr/bin/python3
"""module inherits from."""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited,return true."""
    if not type(obj) is a_class:
        return isinstance(obj, a_class)
