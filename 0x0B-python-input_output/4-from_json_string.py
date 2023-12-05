#!/usr/bin/python3
"""load json format to py object"""
import json


def from_json_string(my_str):
    """load json format to py object"""

    return json.loads(my_str)
