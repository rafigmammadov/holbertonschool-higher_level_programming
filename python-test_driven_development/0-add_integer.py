#!/usr/bin/python3
"""
Program that adds two integers
"""


def add_integer(a, b=98):
    """
    Function that takes a and b as parameters and adds them
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer")

    casted_a = int(a)
    casted_b = int(b)

    return casted_a + casted_b
