#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning."""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_middle(self):
        """Test when max is in the middle."""
        self.assertEqual(max_integer([1, 2, 10, 4]), 10)

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_same_numbers(self):
        """Test a list with the same numbers."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_float_numbers(self):
        """Test a list with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
