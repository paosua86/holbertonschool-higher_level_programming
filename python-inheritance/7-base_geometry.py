#!/usr/bin/python3
"""
Contains class BaseGeometry
"""


class BaseGeometry():
    """calculate area"""
    def area(self):
        raise Exception("area() is not implemented")

    """validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
