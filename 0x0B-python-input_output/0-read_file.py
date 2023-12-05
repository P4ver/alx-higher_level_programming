#!/usr/bin/python3
"""read file name."""


def read_file(filename=""):
    """function reads fl."""
    with open(filename, "r") as fl_nm:
        rd_fl = fl_nm.read()
    print(rd_fl.strip())
