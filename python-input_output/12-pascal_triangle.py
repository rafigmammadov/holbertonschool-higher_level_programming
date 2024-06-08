#!/usr/bin/python3
"""
Module that contains pascal_triangle() function
"""


def pascal_triangle(n):
    """
    Function that returns Pascal triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    return triangle
