#!/usr/bin/python3
"""read file name."""


def read_file(filename=""):
    """function reads fl."""
    with open("my_file_0.txt", "r") as fl_nm:
        rd_fl = fl_nm.read()
    print(rd_fl.strip())
