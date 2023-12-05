#!/usr/bin/python3
"""write file modl."""


def append_write(filename="", text=""):
    """returns lenght of the txt."""
    with open(filename, "a", encoding="utf-8") as fl_a:
        fl_a.write(text)
    return len(text)
