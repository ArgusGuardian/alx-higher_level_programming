#!/usr/bin/python3
"""Define a class mylist and function print sorted"""


class MyList(list):
    """Mylist class inhereted list attributes"""

    def print_sorted(self):
        """print sorted method"""
        print(sorted(self))
