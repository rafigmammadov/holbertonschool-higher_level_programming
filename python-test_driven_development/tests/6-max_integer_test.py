#!/usr/bin/python3
"""
Module that contains tests for "6-max_integer.py" module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestsMaxInteger(unittest.TestCase):
    """
    Class that tests most things
    """

    def test_return(self):
        """
        Test that checks if function returns right answer
        """
        self.assertAlmostEqual(max_integer([1, 3, 5, 7, 9]), 9)

    def test_argument(self):
        """
        Test that checks if return type is integer or not
        """
        self.assertIsInstance(max_integer([1, 2, 3]), int)

    def test_no_parameter(self):
        """
        Test that checks function with no parameter
        """
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """
        Test that checks argument with one element
        """
        self.assertEqual(max_integer([17]), 17)

    def test_negatives(self):
        """
        Test that checks with list that contains only negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_in_the_middle(self):
        """
        Test that checks if max integer is in the middle of the list or not
        """
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)


if __name__ == "__main__":
    unittest.main()
