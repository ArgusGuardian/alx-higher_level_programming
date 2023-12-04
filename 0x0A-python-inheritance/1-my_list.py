#!/usr/bin/python3
"""Define a class mylist and function print sorted"""


class MyList(list):
    """Mylist class inhereted list attributes"""

    def __init__(self):
        """init the onject"""
        super().__init__()

    def print_sorted(self):
        """print sorted method"""
        print(sorted(self))
