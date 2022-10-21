#!/usr/bin/python3
"""test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_base(unittest.TestCase):
    def test_assigning_automatically_an_ID_exists(self):
        self.assertEqual(Base().id, 1)

    def test_assigning_automatically_an_ID_exists_1_previous_exists(self):
        self.assertEqual(Base().id, 2)

    def test_saving_the_ID_passed_exists(self):
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), id, "[]")

    def test_assigning_automatically_an_ID_exists(self):
        self.assertEqual(Base().id, 1)

    def test_assigning_automatically_an_ID_exists(self):
        self.assertEqual(Base().id, 1)

