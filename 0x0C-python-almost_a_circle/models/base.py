#!/usr/bin/python3
"""Module base"""


class Base:
    """Block define the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
