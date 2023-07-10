#!/usr/bin/python3
"""add a new attribute if valid"""


def add_attribute(obj, att, value):
    """..."""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
