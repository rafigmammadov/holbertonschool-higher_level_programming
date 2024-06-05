#!/usr/bin/python3
"""
Module that contains from_json_string() function
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string
    """

    return json.loads(my_str)
