#!/usr/bin/python3
"""Mylist module"""


class MyList(list):
    """repsenting mylist clss."""
    def print_sorted(self):
        """methode sorts elemnt of the lst."""
        print(sorted(self))
