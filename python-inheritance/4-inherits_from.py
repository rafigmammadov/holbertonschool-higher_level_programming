#!/usr/bin/python3
"""
Module that contains inherits_from() function
"""


def inherits_from(obj, a_class):

    """
    Function that returns True if the object is
    an instance of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.
    """

    return not type(obj) is a_class and isinstance(obj, a_class)
