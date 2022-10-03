#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The module contains one function, add_integer(a. b)
"""


def add_integer(a, b=98):
    """Return de addition of two integers"""
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return int(a) + int(b)
    return result
