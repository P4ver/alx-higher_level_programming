#!/usr/bin/python3
"""Mylist module"""


class MyList(list):
    def append(self, vl_apnd):
        """this add elemnt to the list."""
        super().append(vl_apnd)

    def print_sorted(self):
        """methode sorts elemnt of the lst."""
        print(sorted(self))
