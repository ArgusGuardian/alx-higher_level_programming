#!/usr/bin/python3
"""Module base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
