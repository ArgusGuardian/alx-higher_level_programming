#!/usr/bin/python3
"""module for the append function"""


def append_after(filename="", search_string="", new_string=""):
    """function that appends new_string to a line"""
    with open(filename, 'r', encoding='utf-8') as file:
        line = []
        while True:
            line = file.readline()
            if line == "":
                break
            line.append(line)
            if search_string in line:
                line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line)
