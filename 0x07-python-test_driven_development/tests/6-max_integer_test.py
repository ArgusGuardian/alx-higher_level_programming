#!/usr/bin/python3
import unittest

func_module = __import__('6-max_integer')
func = func_module.max_integer


class TestMaxFunc(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(func(""), None)

    def test_str(self):
        string = "Alaaeddine"
        self.assertEqual(func(string), 'n')

    def test_double_array(self):
        strings = ["Alaaeddine", "is", "bateman"]
        self.assertEqual(func(strings), "is")

    def test_decimals(self):
        floats = [-8030, 2.4, 1.2, 2.0, 1000.1]
        self.assertEqual(func(floats), 1000.1)

    def test_mix(self):
        ints_and_floats = [1, 60.5, -90, 12, 16]
        self.assertEqual(func(ints_and_floats), 60.5)

    def test_nothing_list(self):
        empty = []
        self.assertEqual(func(empty), None)

    def test_solo(self):
        one_element = [2]
        self.assertEqual(func(one_element), 2)

    def test_sorted_list(self):
        ordered = [10, 50, 70, 100]
        self.assertEqual(func(ordered), 100)

    def test_unsorted_list(self):
        unordered = [53, 52, 32, 12]
        self.assertEqual(func(unordered), 53)

    def test_max_first(self):
        max_at_beginning = [400, 100, 20, 10]
        self.assertEqual(func(max_at_beginning), 400)

    def test_nothing_list(self):
        empty = []
        self.assertEqual(func(empty), None)

    def test_solo(self):
        one_element = [2]
        self.assertEqual(func(one_element), 2)


if __name__ == '__main__':
    unittest.main()
