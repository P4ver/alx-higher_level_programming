#!/usr/bin/python3
"""Defin json sv obj."""
import json


def save_to_json_file(my_obj, filename):
    """fnction creats newfiles."""
    with open(filename, "w") as fl_sv:
        fl_sv.write(json.dumps(my_obj))
