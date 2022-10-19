#!/usr/bin/python3
"""
Contains the "Base" class
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        filename = cls.__name__+".json"
        if list_objs is not None:
            for i in list_objs:
                list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
