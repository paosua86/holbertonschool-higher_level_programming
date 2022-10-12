#!/usr/bin/python3
"""
contains save_to_json_file fuction
"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a
    JSON representation"""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
