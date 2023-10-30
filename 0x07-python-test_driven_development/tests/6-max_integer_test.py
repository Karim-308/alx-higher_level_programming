#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_single_number(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            max_integer(["string", 2, 3])

    # ... add more tests as needed ...

if __name__ == '__main__':
    unittest.main()
