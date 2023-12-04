#!/usr/bin/python3
"""geo module,"""


class BaseGeometry:
    """empty class."""
    def area(self):
        """display exceptation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """funct that validate vlue."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
