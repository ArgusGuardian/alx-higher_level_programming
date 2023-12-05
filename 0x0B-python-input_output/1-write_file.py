#!/usr/bin/python3
"""function that wirtes to file"""


def write_file(filename="", text=""):
    """function that writes to file and return number of chars"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
