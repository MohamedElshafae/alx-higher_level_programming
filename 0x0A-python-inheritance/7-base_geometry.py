#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """..."""
    def area(self):
        """not impelementd"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ instance method that validates value"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
