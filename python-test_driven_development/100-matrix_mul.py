#!/usr/bin/python3
"""
Module that contains matrix_mul() function
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices:
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(k, (int, float)) for i in m_a for k in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(k, (int, float)) for i in m_b for k in i):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_list = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result_list[i][j] += m_a[i][k] * m_b[k][j]

    return result_list
