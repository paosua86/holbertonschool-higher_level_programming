#!/usr/bin/python3
"""
Contains the "Base" class
"""


class Base:
    """Bse class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
