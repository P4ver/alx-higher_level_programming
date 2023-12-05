#!/usr/bin/python3
"""Define json frm str to another obj."""
import json


def from_json_string(my_str):
    """return obj from str."""
    return json.loads(my_str)
