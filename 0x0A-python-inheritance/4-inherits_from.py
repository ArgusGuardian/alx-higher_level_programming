#!/usr/bin/python3
"""define function to check inherited class"""


def inherits_from(obj, a_class):
    """function to check iniretance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
