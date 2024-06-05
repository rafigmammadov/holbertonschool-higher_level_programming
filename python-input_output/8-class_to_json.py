#!/usr/bin/python3
"""
Module that contains class_to_json() function
"""
import json


def class_to_json(obj):
    """
    function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    return json.dumps(obj.__dir__)
