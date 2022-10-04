#!/usr/bin/python3
"""
This is the "2-matrix_divider" module.

The module contains one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    matrix_1 = []
    for x in matrix:    
        matrix_1.append(list(map(lambda y: round(y / div, 2), x)))
    return matrix_1
