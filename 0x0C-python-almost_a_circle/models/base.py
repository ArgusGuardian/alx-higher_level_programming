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
        """static method to to convert dict to str"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method save str to file"""
        f = cls.__name__+".json"
        with open(f, "w") as json_f:
            if not list_objs:
                json_f.write("[]")
            else:
                dicts = [num.to_dictionary() for num in list_objs]
                json_f.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """static method to load dicts from json file"""
        if not json_string or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class with **dictionary asa aguments"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
