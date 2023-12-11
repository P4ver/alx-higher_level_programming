#!/usr/bin/python3
"""module base."""


import json


class Base:
    """Representing base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json str repesentaion of list_dict."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method wirtes json str."""
        if list_objs is not None:
            list_objs = [b.to_dictionary() for b in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as pvr:
            pvr.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns list of json str representtion."""
        if json_string is None or not json_string:
            return []
        else:
            return eval(json_string)
