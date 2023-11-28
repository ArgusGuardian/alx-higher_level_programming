#!/usr/bin/python3
"""Defines locked class"""


class LockedClass:
    """
    this class will refuse to create any instance not named
    'first name'
    """
    __slots__ = ('first_name',)
