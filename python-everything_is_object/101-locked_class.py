#!/usr/bin/python3
"""Write a class LockedClass"""


class LockedClass:
    """prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute is
    called first_name"""
    __slot__ = ["fist_name"]
