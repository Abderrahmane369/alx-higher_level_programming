#!/usr/bin/python3
"""tests of all files"""
import unittest
from models.square import Square


class TestsOFAllFiles(unittest.TestCase):
    """All cases"""

    def test_Normal(self):
        square = Square(5, 100, 100, 20313)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 100)
        self.assertEqual(square.y, 100)
        self.assertEqual(square.id, 20313)

    def test_NoId(self):
        square = Square(5, 100, 100)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 100)
        self.assertEqual(square.y, 100)
        self.assertTrue(square.id is not None)

    def test_No_y(self):
        square = Square(5, 100, id=1234)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 100)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 1234)

    def test_No_y(self):
        square = Square(5, y=100, id=1234)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 100)
        self.assertEqual(square.id, 1234)

    def test_No_x(self):
        square = Square(5, y=100, id=1234)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 100)
        self.assertEqual(square.id, 1234)

    def test_size(self):
        with self.assertRaises(ValueError):
            square = Square(-10, 100, 5, 5123)

        with self.assertRaises(ValueError):
            square = Square(0, 100, 5, 5123)

    def test_xy_under0(self):
        with self.assertRaises(ValueError):
            square = Square(10, -12, 23, 43121)

        with self.assertRaises(ValueError):
            square = Square(10, 12, -23, 43121)

    def test_MoreArgs(self):
        with self.assertRaises(TypeError):
            quare = Square(1, 1, 1, 1, 1)

    def test_xy_under0(self):
        with self.assertRaises(ValueError):
            square = Square(10, -12, 23, 43121)

        with self.assertRaises(ValueError):
            square = Square(10, 12, -23, 43121)

    def test_setter_size(self):
        with self.assertRaises(ValueError):
            square = Square(10, 10, 10, 101010)
            square.size = 0

        with self.assertRaises(ValueError):
            square = Square(10, 10, 10, 101010)
            square.size = -5

    def test_str(self):
        square = Square(1, 23, 4, 1)
        self.assertEqual(square.__str__(), '[Square] (1) 23/4 - 1')

        square = Square(1, 23, 4)
        self.assertEqual(square.__str__(), '[Square] (2) 23/4 - 1')

    def test_update(self):
        square = Square(10, 2, 3, 5555)
        square.update(555, 20, 5, 6)
        self.assertEqual(square.id, 555)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 5 + 1)

        square = Square(10, 2, 3, 5555)
        square.update(555, 20, 5)
        self.assertEqual(square.id, 555)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 3)

        square = Square(10, 2, 3, 5555)
        square.update(555, 20)
        self.assertEqual(square.id, 555)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        square = Square(10, 2, 3, 5555)
        square.update(555)
        self.assertEqual(square.id, 555)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        square = Square(10, 2, 3, 5555)
        square.update()
        self.assertEqual(square.id, 5555)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        square = Square(1, 3, 4, 5555)
        with self.assertRaises(ValueError):
            square.update(555, -1, 5, 5)
            square.update(555, 0, 5, 5)
            square.update(555, 5, -5, 5)
            square.update(555, "3", 5, -5)
            square.update(555, 5, "2", 5)
            square.update(555, 5, 3, "5")

        square = Square(1, 2, 3, 5555)
        square.update(size=2, x=6, y=8, id=6666, a=232)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 1111 * 6)

        with self.assertRaises(AttributeError):
            self.assertEqual(square.a, 232)

        square = Square(1, 2, 3, 5555)
        square.update(size=2, x=6, y=8, id=6666)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 1111 * 6)

        square = Square(1, 2, 3, 5555)
        square.update(size=2, x=6, y=8)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)

        square = Square(1, 2, 3, 5555)
        square.update(size=2, x=6)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 6)

        square = Square(1, 2, 3, 5555)
        square.update(size=2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)

        square = Square(1, 2, 3, 5555)
        square.update(size=2, a=5)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.height, 2)

        square = Square(1, 3, 4, 5555)
        with self.assertRaises(ValueError):
            square.update(size=-5, x=6, y=8, id=6666)
            square.update(size=5, x=-6, y=8, id=6666)
            square.update(size=5, x=6, y=-8, id=6666)
            square.update(size=5, x=6, y="8", id=6666)
            square.update(size=5, x="6", y=8, id=6666)
            square.update(size="a", x=6, y=8, id=6666)

        with self.assertRaises(AttributeError):
            self.assertEqual(square.a, 5)

        square = Square(1, 2, 3, 5555)
        square.update(w=5)

        with self.assertRaises(AttributeError):
            self.assertEqual(square.w, 5)

        square = Square(1, 2, 3, 5)
        square.update(2, 3, 5, 7, 213)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 7)
        self.assertEqual(square.id, 2)

    def test_to_dictionnary(self):
        square = Square(1, 2, 3, 5)
        self.assertEqual(square.to_dictionary(),
                         {'size': 1,
                          'x': 2, 'y': 3, 'id': 5})

        square = Square(1, 2, 3)
        self.assertEqual(square.to_dictionary(),
                         {'size': 1,
                          'x': 2, 'y': 3, 'id': 3})
