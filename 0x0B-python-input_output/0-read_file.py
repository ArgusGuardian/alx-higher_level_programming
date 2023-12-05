#!/usr/bin/python3
"""Function open and print content"""


def read_file(filename=""):
    """function that opens and prints content"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
