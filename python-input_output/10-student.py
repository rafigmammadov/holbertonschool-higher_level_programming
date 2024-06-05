#!/usr/bin/python3
"""
Module that contains Student class
"""


class Student:
    """
    class Student that contains some methods
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return {key: value for key, value in self.__dict__.items()
                if attrs is None or key in attrs}
