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
        return self.__dict__
