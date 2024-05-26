#!/usr/bin/python3
"""
Documentation for Square class module
"""


class Square:
    """
    Square class that only has size attribute with some additional checks
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
