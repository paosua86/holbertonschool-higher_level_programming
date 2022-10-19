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
    def to_json_string(list_dictorionaries):
        """ returns the JSON string representation"""
        if list_dictorionaries is None:
            return "[]"
        return json.dumps(list_dictorionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        filename = cls.__name__ + ".json"
        list = []
        if list_objs is None:
            return "[]"
        for i in list_objs:
            list.append(cls.to_dictionary(i))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))
