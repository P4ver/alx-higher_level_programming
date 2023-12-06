#!/usr/bin/python3
"""module stdnt json."""


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
