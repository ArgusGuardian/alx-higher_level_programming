#!/usr/bin/python3
"""Defines unittests for Base class"""
import os
import unittest
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class TestBase_init(unittest.TestCase):
    def test_0_arg(self):
        f1 = Base()
        f2 = Base()
        self.assertEqual(f1.id, f2.id - 1)
