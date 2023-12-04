#!/usr/bin/python3
"""defines int inhereted class"""


class MyInt(int):
    """class MyInt that inheretes from int"""
    def __new__(cls, *args, **kwargs):
        """rebel the versioin of integer"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """not is now is"""
        return int(self) != other

    def __ne__(self, other):
        """bypolar discussion"""
        return int(self) == other
