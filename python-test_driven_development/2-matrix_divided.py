#!/usr/bin/python3
"""
This is the "2-matrix_divider" module.

The module contains one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be an number")
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if isinstance(row, list) and row:
            for col in row:
                if not isinstance(col, int) and not isinstance(col, float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    matrix_1 = []
    for x in matrix:
        matrix_1.append(list(map(lambda y: round(y / div, 2), x)))
    return matrix_1
