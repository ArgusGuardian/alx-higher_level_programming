#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, 'count', -1) + 1
    return 'BestSchool' + ', BestSchool' * magic_string.counter
