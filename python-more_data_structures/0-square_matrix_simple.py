#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []

    for i in matrix:
        result_matrix.append(list(map(lambda x: x**2, i)))

    return result_matrix
