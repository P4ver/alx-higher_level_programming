#!/usr/bin/python3
"""define json creat obj."""
import json


def load_from_json_file(filename):
    """returns obj that was created."""
    with open(filename, "r") as fl_ro:
        q = json.load(fl_ro)
    return q
