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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
