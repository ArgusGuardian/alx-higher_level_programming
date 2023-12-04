#!/usr/bin/python3
"""defines a function that adds attribute to object."""


def add_attribute(obj, att, value):
    """add attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
