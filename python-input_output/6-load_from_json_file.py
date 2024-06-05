#!/usr/bin/python3
"""
Module that contains load_from_json_file() function
"""
import json


def load_from_json_file(filemame):
    """
    Function that creates an Object from a “JSON file”
    """

    with open(filemame, 'r', encoding="utf-8"):
        json.loads(filemame.read())
