#!/usr/bin/python3
"""write file modl."""


def write_file(filename="", text=""):
    """returns lenght of the txt."""
    with open(filename, "w", encoding="utf-8") as fl_w:
        fl_w.write(text)
    return len(text)
