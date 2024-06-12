#!/usr/bin/python3
"""
Module that handles serialization operation
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Function that serializes and saves to the object
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    Function that deserializes from the object
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
