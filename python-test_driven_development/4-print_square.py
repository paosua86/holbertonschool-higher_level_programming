#!/usr/bin/python3
"""
This is the "2-matrix_divider" module.

The module contains one function, matrix_divided(matrix, div)
"""


def print_square(size):
    """Write a function that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
