#!/usr/bin/python3
"""tests"""

import unittest
from models.rectangle import Rectangle
import os

class TestRectangle(unittest.TestCase):
    """test of class Rectangle"""

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

    def test_rectangle_creation_4(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, height = "1")
        self.assertRaises(TypeError, Rectangle, width = "2")
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
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):
        rect_1 = Rectangle(6, 2)
        self.assertEqual(rect_1.area(), 12)

    def test_rectangle_representation(self):
        rect_repr = str(Rectangle(1, 2, 3, 4, 5))
        result = '[Rectangle] (5) 3/4 - 1/2'
        self.assertEqual(rect_repr, result)

    def test_rectangle_to_dictionary_exists(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        result = {
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
            'id': 5
        }
        self.assertEqual(rect_dict, result)

    def test_rectangle_update_exists_1(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_2(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_3(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_4(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_exists_5(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_6(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_7(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_8(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_9(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_create_exists_1(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89})

    def test_rectangle_create_exists_2(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': 1})

    def test_rectangle_create_exists_3(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_create_exists_4(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_create_exists_5(self):
        rect = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
        })
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_save_to_file_exists_none(self):
        Rectangle.save_to_file(None)

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove('Rectangle.json')

    def test_rectangle_save_to_file_exists_empty(self):
        Rectangle.save_to_file([])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove('Rectangle.json')

    def test_rectangle_save_to_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]')
        os.remove('Rectangle.json')

    def test_rectangle_load_from_file_not_exists(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2, 1, 1, 5)])
        lst_obj = Rectangle.load_from_file()

        self.assertEqual(lst_obj[0].width, 1)
