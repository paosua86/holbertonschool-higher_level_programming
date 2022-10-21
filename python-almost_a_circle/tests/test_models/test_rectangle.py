#!/usr/bin/python3
"""test"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    '''contains all test of class Rectangle'''

    def test_rectangle_creation_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_creation_2(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_creation_3(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_creation_3(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, width = '2')
        self.assertRaises(TypeError, Rectangle, width = float('NaN'))
        self.assertRaises(TypeError, Rectangle, width = float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, height = 'abc')
        self.assertRaises(TypeError, Rectangle, 1, 1, x = {})
        self.assertRaises(TypeError, Rectangle, 1, 1, y = 2.5)

    def test_value(self):
        '''width, height, x, y'''
        self.assertRaises(ValueError, Rectangle, -5, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -565)
        self.assertRaises(ValueError, Rectangle, 1, 1, -755)
        self.assertRaises(ValueError, Rectangle, 1, 1, -2)

    def test_area(self):
        rect_1 = Rectangle(6, 2)
        self.assertEqual(rect_1.area(), 12)
