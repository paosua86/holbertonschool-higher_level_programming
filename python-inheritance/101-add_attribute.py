#!/usr/bin/python3
"""adds a new attribute to an object if it is possible"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
