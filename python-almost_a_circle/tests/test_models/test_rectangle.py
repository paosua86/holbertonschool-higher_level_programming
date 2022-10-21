#!/usr/bin/python3
'''
test_models/test_rectangle module
test if the class rectangle is functional
try test with python3 -m unittest discover test at
0x0C-python-almost_a_circle directory
'''


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    '''contains all test of class Rectangle'''

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
