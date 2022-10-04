#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)
        
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_positives(self):
        """Testing positive numbers"""

        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

        list = [5, 2, 3, 4, 1]
        self.assertEqual(max_integer(list), 5)

        list = [1, 2, 6, 4, 5]
        self.assertEqual(max_integer(list), 6)

        list = [3, 3, 3, 3]
        self.assertEqual(max_integer(list), 3)

        list = [1.1, 1.2, 1.3, 1.4]
        self.assertEqual(max_integer(list), 1.4)

        list = [1]
        self.assertEqual(max_integer(list), 1)


    def test_negatives(self):
        """Testing negative numbers"""

        list = [-1, 2, -3, -4]
        self.assertEqual(max_integer(list), 2)

        list = [-5, -2, -3, -1]
        self.assertEqual(max_integer(list), -1)

        list = [-2]
        self.assertEqual(max_integer(list), -2)

        list = [-5, -2, -3, -1]
        self.assertEqual(max_integer(list), -1)

    def test_none_and_zero(self):
        """Testing none and zero"""
        
        list = []
        self.assertEqual(max_integer(list), None)

        list = [0, 0, 0]
        self.assertEqual(max_integer(list), 0)

        self.assertEqual(max_integer(), None)

    def test_other_than_numbers(self):
        """Testing other than numbers"""

        list = [0, "hello", 0]
        self.assertRaises(TypeError)

        list = [0, [1, 2], 0]
        self.assertRaises(TypeError)

        list = [0, (1, 2), 0]
        self.assertRaises(TypeError)

if __name__ == "__main__":
    unittest.main()
