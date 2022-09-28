#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents a square
    Attributes_
        size (int): square size.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
