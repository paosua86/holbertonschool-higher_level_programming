#!/usr/bin/python3
from operator import length_hint


def replace_in_list(my_list, idx, element):
    if 0 <= idx and len(my_list) > idx:
        my_list[idx] = element
    return (my_list)
