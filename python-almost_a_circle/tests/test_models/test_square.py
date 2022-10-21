#!/usr/bin/python3
"""tests"""

import unittest
from models.square import Square

class Testsquare(unittest.TestCase):
    """test of class S"""

    def test_square_creation_1(self):
        rect = Square(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_square_creation_2(self):
        rect = Square(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
