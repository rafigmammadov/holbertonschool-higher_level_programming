#!/usr/bin/python3
"""
Module that contains text_indentation() function
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for i in text:
        result += i

        if i in {'.', '?', ':'}:
            result += '\n\n'

    print("\n".join(i.strip() for i in result.split("\n")), end="")
