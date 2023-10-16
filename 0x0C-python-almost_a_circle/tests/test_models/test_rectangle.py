#!/usr/bin/python3
"""tests of all files"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


class TestsOFAllFiles(unittest.TestCase):
    """All cases"""

    def test_Normal(self):
        rect = Rectangle(10, 100, 1, 11, 32923)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 100)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 11)
        self.assertEqual(rect.id, 32923)

    def test_NoId(self):
        rect = Rectangle(10, 100, 1, 11)
        self.assertEqual(rect.id, 1)
        rect = Rectangle(10, 1002, 1, 11)
        self.assertEqual(rect.id, 2)
        rect = Rectangle(10, 1100, 1, 11)
        self.assertEqual(rect.id, 3)
        rect = Rectangle(10, 1050, 1, 11)
        self.assertEqual(rect.id, 4)

    def test_no_x(self):
        rect = Rectangle(10, 100, y=2, id=2131)
        self.assertEqual(rect.x, 0)

    def test_no_y(self):
        rect = Rectangle(10, 100, x=2, id=2131)
        self.assertEqual(rect.y, 0)

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 100, -5, 5, 5123)

    def test_y_neg(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 100, 5, -5, 5123)

    def test_x_zero(self):
        rect = Rectangle(23, 32, 0, 5, 23113)
        self.assertEqual(rect.x, 0)

    def test_y_zero(self):
        rect = Rectangle(23, 32, 10, 0, 23113)
        self.assertEqual(rect.y, 0)

    def test_notIntger_attr(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("10", 10, 10, 10, 101101)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, "10", 10, 10, 11010)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, 10, "10", 10, 1001010)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, 10, 10, "10", 1001010)

    def test_width_height_equal_0_or_neg(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10, 5, 5, 5321)

        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 10, 5, 5, 5321)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0, 5, 5, 5321)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, -10, 5, 5, 5321)

    def test_xy_under0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 10, -12, 23, 43121)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 10, 12, -23, 43121)

    def test_setter_size(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 10, 10, 10, 101010)
            rectangle.width = 0

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 10, 10, 10, 101010)
            rectangle.width = -5

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 10, 10, 10, 101010)
            rectangle.height = 0

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 10, 10, 10, 101010)
            rectangle.height = -5

    def test_MoreArgs(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 1, 1, 1, 1, 1)

    def test_area(self):
        rect = Rectangle(3, 2, 1000, 100, 10)
        self.assertEqual(rect.area(), 6)

        rect = Rectangle(1, 2, 1000, 100, 10)
        self.assertEqual(rect.area(), 2)

    def test_display(self):
        rect = Rectangle(3, 6, 0, 0, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "###\n" * 6)

        rect = Rectangle(1, 1, 0, 0, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "#\n")

        rect = Rectangle(2, 1, 0, 0, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "##\n")

        rect = Rectangle(1, 4, 0, 0, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "#\n" * 4)

        rect = Rectangle(2, 4, 3, 3, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "\n" * 3 + (" " * 3 + "##\n") * 4)

        rect = Rectangle(2, 4, 2, 6, 5555)

        with patch("sys.stdout", new_callable=io.StringIO) as mstd:
            rect.display()

            output = mstd.getvalue()

        self.assertEqual(output, "\n" * 6 + (" " * 2 + "##\n") * 4)

    def test_str(self):
        rect = Rectangle(1, 23, 4, 1, 11235)
        self.assertEqual(rect.__str__(), '[Rectangle] (11235) 4/1 - 1/23')

        rect = Rectangle(1, 23, 4, 1)
        self.assertEqual(rect.__str__(), '[Rectangle] (5) 4/1 - 1/23')

    def test_update(self):
        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(2, 3, 5, 7, 1111)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 1111)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(2, 3, 5, 7)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(2, 3, 5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(2, 3)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update()
        self.assertEqual(rect.id, 5555)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        with self.assertRaises(ValueError):
            rect.update(-1, 2, 3, 4, 5555)
            rect.update(1, -2, 3, 4, 5555)
            rect.update(0, 2, 3, 4, 5555)
            rect.update(1, 0, 3, 4, 5555)
            rect.update(1, 2, -5, 4, 5555)
            rect.update(1, 2, 3, -5, 5555)
            rect.update("aas", 2, 3, 5, 5555)
            rect.update(2, "2", 3, 5, 5555)
            rect.update(2, 2, "3", 5, 5555)
            rect.update(2, 2, 3, "5", 5555)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4, x=6, y=8, id=6666, a=232)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 8)
        self.assertEqual(rect.id, 1111 * 6)

        with self.assertRaises(AttributeError):
            self.assertEqual(rect.a, 232)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4, x=6, y=8, id=6666)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 8)
        self.assertEqual(rect.id, 1111 * 6)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4, x=6, y=8)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 8)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4, x=6)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 6)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2)
        self.assertEqual(rect.width, 2)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(width=2, height=4, a=5)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)

        with self.assertRaises(AttributeError):
            self.assertEqual(rect.a, 5)

        rect = Rectangle(1, 2, 3, 4, 5555)
        rect.update(w=5)

        with self.assertRaises(AttributeError):
            self.assertEqual(rect.w, 5)

        with self.assertRaises(ValueError):
            rect.update(width=-2, height=4, x=6, y=8, id=6666)
            rect.update(width=2, height=-4, x=6, y=8, id=6666)
            rect.update(width=0, height=4, x=6, y=8, id=6666)
            rect.update(width=2, height=0, x=6, y=8, id=6666)
            rect.update(width=2, height=4, x=-1, y=8, id=6666)
            rect.update(width=2, height=4, x=6, y=-1, id=6666)
            rect.update(width="a", height=4, x=6, y=-1, id=6666)
            rect.update(width=2, height="4", x=6, y=-1, id=6666)
            rect.update(width=2, height=4, x="6", y=-1, id=6666)
            rect.update(width=2, height=4, x=6, y=-"1", id=6666)

        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(2, 3, 5, 7, 1111, 213)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 1111)
        self.assertEqual(rect.id, 2)

    def test_to_dictionnary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.to_dictionary(),
                         {'width': 1, 'height': 2,
                          'x': 3, 'y': 4, 'id': 5})

        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.to_dictionary(),
                         {'width': 1, 'height': 2,
                          'x': 3, 'y': 4, 'id': 6})
