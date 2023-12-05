#!/usr/bin/python3
"""student class module"""


class Student:
    """define a Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict reprsentation of student instance"""
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        if json['first_name']:
            self.first_name = json['first_name']
        if json['last_name']:
            self.last_name = json['last_name']
        if json['age']:
            self.age = json['age']
