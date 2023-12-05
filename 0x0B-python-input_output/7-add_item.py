#!/usr/bin/python3
"""script tha laods from file appends then saves to json file"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    new = load_from_json_file('add_item.json')
except FileNotFoundError:
    new = []

for element in argv[1:]:
    new.append(element)

save_to_json_file(new, 'add_item.json')
