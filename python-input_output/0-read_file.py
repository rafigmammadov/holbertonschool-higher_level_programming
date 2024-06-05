#!/usr/bin/python3
"""
Module that contains function read_file() function
"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == "__main__":
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")
