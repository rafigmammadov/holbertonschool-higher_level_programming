#!/usr/bin/python3
"""
Module that contains class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size * self.__size
