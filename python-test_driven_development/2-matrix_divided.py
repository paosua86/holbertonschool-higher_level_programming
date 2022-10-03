#!/usr/bin/python3
"""
This is the "2-matrix_divider" module.

The module contains one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if isinstance(row, list) and row:
            for col in row:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
