#!/usr/bin/python3
"""module stdnt json."""


class Student:
    """repesent a stdnt with frst and last name and age."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """funct that retrieves a dict representation of a stdnt."""
        if attrs is None:
            return self.__dict__
        else:
            fl={}
            for at_tr in attrs:
                if hasattr(self, at_tr):
                    fl[at_tr] = getattr(self, at_tr)
        return fl
