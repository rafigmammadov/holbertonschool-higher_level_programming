#!/usr/bin/python3
"""
Module that contains print_square() function
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    size = int(size)

    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
