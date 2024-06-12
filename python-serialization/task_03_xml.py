#!/usr/bin/python3
"""
Module that contains functions for serializing
and deserializing from XML tables
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function that serialize the dictionary into
    XML and save it to the given filename
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child_tag = ET.SubElement(root, key)
        child_tag.text = str(value)

    ET.ElementTree(root).write(filename, encoding='utf-8',
                               xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function that read the XML data from
    that file and return a deserialized Python dictionary
    """

    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}

    for child_tag in root:
        dict[child_tag.tag] = child_tag.text

    return dict
