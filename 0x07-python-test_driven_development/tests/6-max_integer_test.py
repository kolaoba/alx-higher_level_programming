#!/usr/bin/python3
"""Unittests for max_integer(list)"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define unittests for max_integer(list)
    """

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [2, 4, 5, 8, 67]
        self.assertEqual(max_integer(ordered), 67)
    
    def test_unorered_list(self):
        """Test an unordered list of integers"""
        unordered = [32, 55, 29, 48, 56]
        self.assertEqual(max_integer(unordered), 56)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_the_beginning(self):
        """Tests when max at beginning of list"""
        max_list = [500, 2, 5, 490, 85]
        self.assertEqual(max_integer(max_list), 500)

    def test_single_element_list(self):
        """Test a single element list"""
        single = [10]
        self.assertEqual(max_integer(single), 10)

    def test_list_with_floats(self):
        """Test a list of floats"""
        floats = [1.2, 5.8, 3.5, 9.5, 0.2]
        self.assertEqual(max_integer(floats), 9.5)

    def test_list_with_ints_and_floats(self):
        """Test a list of a mix of ints and floats"""
        mix = [50, 97.9, 24.53, 100, 105.3]
        self.assertEqual(max_integer(mix), 105.3)

    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["Totally", "a", "list", "of", "numbers"]
        self.assertEqual(max_integer(strings), "of")

    def test_empty_strings(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
