#!/usr/bin/python3
"""
Module that contains append_after() function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to
    a file, after each line containing a specific string
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for index, line in enumerate(lines):
            if search_string in line:
                lines.insert(index + 1, new_string + '\n')

        file.seek(0)

        file.writelines(lines)
