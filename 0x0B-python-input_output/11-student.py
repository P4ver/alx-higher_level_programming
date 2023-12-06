#!/usr/bin/python3
"""define stdnt to disk reload."""


class Student:
    """repesent a stdnt with frst and last name and age."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """funct that retrieves a dict representation of a stdnt."""
        if attrs is None:
            return self.__dict__
        else:
            fl = {}
            for q, u in self.__dict__.items():
                if q in attrs:
                    fl[q] = u
            return fl

    def reload_from_json(self, json):
        """ methodes replaces all attr of class stdent instance."""
        for q, p in json.items():
            self.__dict__[q] = p
