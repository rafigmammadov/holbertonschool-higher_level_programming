#!/usr/bin/python3
"""
Module that contains add_attribute() module
"""


def add_attribute(obj, name, val):
    """
    Function that adds a new attribute to an object if it's possible
    """
    if hasattr(obj, "__dict__") or isinstance(obj, (dict, list, set, tuple)):
        setattr(obj, name, val)
    else:
        raise TypeError("can't add new attribute")
