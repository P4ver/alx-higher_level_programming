#!/usr/bin/python3
"""read file name."""


def read_file(filename=""):
    """function reads fl."""
    with open(filename, encoding="utf-8") as fl_nm:
        print(fl_nm.read(), end="")
