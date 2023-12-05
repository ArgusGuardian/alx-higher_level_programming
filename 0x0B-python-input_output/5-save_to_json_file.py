#!/usr/bin/python3
"""function writes json to file"""
import json


def save_to_json_file(my_obj, filename):
    """function writes json to file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
