#!/usr/bin/python3
"""
Program that adds two integers
"""


def add_integer(a, b=98):
    """
    Function that takes a and b as parameters and adds them
    """
    if a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    casted_a = int(a)
    casted_b = int(b)

    return casted_a + casted_b
