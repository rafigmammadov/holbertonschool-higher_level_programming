#!/usr/bin/python3
"""
Documentation for Square class module
"""


class Square:
    """
    Square class that can calculate area with print property
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        square_str = ""
        if self.size == 0:
            return square_str
        for _ in range(self.position[1]):
            square_str += "\n"
        for _ in range(self.size):
            square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str
