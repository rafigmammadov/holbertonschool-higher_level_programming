#!/usr/bin/python3
"""
Program that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    new_matrix = []
    standart_len = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        row_matrix = []
        if len(row) != standart_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")

            row_matrix.append(round(element / div, 2))

        new_matrix.append(row_matrix)

    return new_matrix
