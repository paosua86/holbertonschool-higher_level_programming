#!/usr/bin/python3
'''
test_models/test_base module
test if the class Base is functional
try test with python3 -m unittest discover test at
0x0C-python-almost_a_circle directory
'''


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    '''contains all test of class Base'''

    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(125)
        self.assertEqual(base3.id, 125)
