#!/usr/bin/python3
"""
Module that contains CustomObject class
"""
import pickle


class CustomObject:
    """
    Class that contains some attributes and display method
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}\nAge: {}\nIs student: {}".
              format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, mode="wb") as f:
                f.write(pickle.dumps(self))
        except Exception as e:
            print("An error occured: {}".format(e))

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, mode="rb") as f:
                return pickle.loads(f.read())
        except Exception as e:
            print("An error occured: {}".format(e))
            return None
