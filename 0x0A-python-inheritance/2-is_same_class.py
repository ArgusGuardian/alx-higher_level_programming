#!/usr/bin/python3
"""difines function to check object class"""


def is_same_class(obj, a_class):
    """function to compare object class with class"""
    if type(obj) == a_class:
        return True
    else:
        return False
