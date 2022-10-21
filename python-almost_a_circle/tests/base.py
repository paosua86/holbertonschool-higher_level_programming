#!/usr/bin/python3
"""test"""

import unittest
from models import Rectangle

class Base_Test(unittest.TestCase):
    """test all"""


    def test0(self):
        """type error"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, "1")

    def test1(self):
        """type error"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1)

    def test_2(self):
        """value error"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 0)

    def test_3(self):
        """value error"""
        with self.assertRaises(TypeError):
            r = Rectangle(0, 1)

    def test_4(self):
        """value error"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, -1)

    def test_5(self):
        """value error"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, -1, 1)

    def test_6(self):
        """Str tests"""
        r = Rectangle(3, 2, 3, 2)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (8) 2/2 - 2/2\n", out.getvalue())
        r = Rectangle(3, 5, 2, 4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (9) 2/4 - 3/1\n", out.getvalue())

    def test_7(self):
        """ Display tests """
        r = Rectangle(2, 3, 3, 1)
        out = self.capture_stdout(r, "display")
        self.assertEqual("\n\n  ##\n  ##\n  ##\n", out.getvalue())
        r = Rectangle(3, 8, 1, 2)
        out = self.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", out.getvalue())
        r = Rectangle(5, 6, 5, 8)
        out = self.capture_stdout(r, "display")
        correct = "\n\n\n\n\n     #####\n     #####\n     #####\n"
        correct += "     #####\n     #####\n"
        self.assertEqual(correct, out.getvalue())

    def test_8(self):
        """ Update tests """
        r = Rectangle(4, 5, 10, 2)
        r.update(89)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10\n", out.getvalue())
        r.update(5, 1)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10\n", out.getvalue())
        r.update(8, 2, 5)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3\n", out.getvalue())
        r.update(5, 6, 3, 4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3\n", out.getvalue())
        r.update(9, 2, 3, 8, 4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3\n", out.getvalue())

        r = Rectangle(5, 5, 5, 5)
        r.update(width=1)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (1) 10/10 - 10/1\n", out.getvalue())
        r.update(width=6, x=2)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (1) 2/10 - 1/1\n", out.getvalue())
        r.update(y=1, width=2, x=3, id=89)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1\n", out.getvalue())
        r.update(x=1, height=2, y=3, width=4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2\n", out.getvalue())
