#!/usr/bin/python3
"""
contains class pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n:"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    list = [[1]]
    while len(list) != n:
        last_n = list[-1]
        new_n = [1]
        for i in range(len(last_n) - 1):
            new_n.append(last_n[i] + last_n[i + 1])
        new_n += [1]
        list.append(new_n)
    return list
