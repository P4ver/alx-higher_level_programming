#!usr/bin/python3
"""base module."""
import json


class Base:
    """Representing base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """returns json str repesentaion of list_dict."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
