#!/usr/bin/python3
"""function that writes to file"""


def append_write(filename="", text=""):
    """function that appends to file and return number of chars"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.append(text)
