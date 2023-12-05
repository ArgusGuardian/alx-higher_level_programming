#!/usr/bin/python3
"""function loads from json file"""

import json


def load_from_json_file(filename):
    """function loads from json file"""
    with open(filename) as file:
        return json.load(file)
