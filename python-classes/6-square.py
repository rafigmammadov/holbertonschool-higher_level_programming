#!/usr/bin/python3
"""
class Square
"""


class Square():
    """
    Private instance attribute: size
    Private instance attribute: position
    Public instance method: def area(self):
    Public instance method: def my_print(self):
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)
           and len(value) == 2
           and isinstance(value[0], int)
           and isinstance(value[1], int)
           and value[0] >= 0
           and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
