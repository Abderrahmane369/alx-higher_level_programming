#!/usr/bin/python3
"""tests of all files"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestsOFAllFiles(unittest.TestCase):
    """All cases"""

    def test_Normal(self):
        base = Base(3249)
        self.assertEqual(base.id, 3249)

    def test_NoId(self):
        base = Base()
        self.assertTrue(base.id is not None)
        base = Base()
        self.assertTrue(base.id is not None)
        base = Base()
        self.assertTrue(base.id is not None)

    def test_ZeroId(self):
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_NegativeId(self):
        base = Base(-1321)
        self.assertEqual(base.id, -1321)

    def test_NoneId(self):
        base = Base(None)
        self.assertTrue(base.id is not None)
        base = Base(None)
        self.assertTrue(base.id is not None)
        base = Base(None)
        self.assertTrue(base.id is not None)

    def test_Mixed(self):
        base = Base()
        self.assertTrue(base.id is not None)
        base = Base(None)
        self.assertTrue(base.id is not None)
        base = Base()
        self.assertTrue(base.id is not None)
        base = Base(5)
        self.assertEqual(base.id, 5)
        base = Base()
        self.assertTrue(base.id is not None)

    def test_greatersArgs(self):
        with self.assertRaises(TypeError):
            base = Base(1, 23)

        with self.assertRaises(TypeError):
            base = Base(1, 23, 2)

    def test_toJSON_String(self):
        base = Base(1)
        self.assertEqual(base.to_json_string([{"1": 1, "2": 2, "3": 3}]),
                         '[{"1": 1, "2": 2, "3": 3}]')

        self.assertEqual(base.to_json_string([{"1": 1}]),
                         '[{"1": 1}]')

        self.assertEqual(base.to_json_string([{}]),
                         '[{}]')

        self.assertEqual(base.to_json_string([]),
                         '[]')

        self.assertEqual(base.to_json_string([2]),
                         '[2]')

        self.assertEqual(base.to_json_string(55),
                         '55')

        self.assertEqual(base.to_json_string("aa"),
                         '"aa"')

        with self.assertRaises(TypeError):
            string = base.to_json_string()

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1000)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            a = '[{"x": 2, "y": 8, "id": 1000, "width": 10, "height": 7}'
            a += ', {"x": 0, "y": 0, "id": 12, "width": 2, "height": 4}]'

            self.assertEqual(file.read(), a)

        r1 = Square(10, 7, 2, 8888)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open("Square.json", "r") as file:
            a = '[{"x": 7, "y": 2, "size": 10, "id": 8888},'
            a += ' {"x": 0, "y": 0, "size": 2, "id": 13}]'

            self.assertEqual(file.read(), a)

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            a = '[]'

            self.assertEqual(file.read(), a)

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            a = '[]'

            self.assertEqual(file.read(), a)

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            a = '[]'

            self.assertEqual(file.read(), a)

        Square.save_to_file([])

        with open("Square.json", "r") as file:
            a = '[]'

            self.assertEqual(file.read(), a)

        with open("Square.json", "r") as file:
            a = '[]'

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([2, 3])

        with open("Rectangle.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Square.save_to_file([2, 3])

        with open("Square.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([{}])

        with open("Rectangle.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Square.save_to_file([{}])

        with open("Square.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([{"a", "b"}])

        with open("Rectangle.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

        with self.assertRaises(AttributeError):
            Square.save_to_file([{"a", "b"}])

        with open("Square.json", "r") as file:
            a = ''

            self.assertEqual(file.read(), a)

    def test_fromJSON_String(self):
        base = Base(10)
        self.assertEqual(base.from_json_string('[{"1": 1, "2": 2, "3": 3}]'),
                         [{"1": 1, "2": 2, "3": 3}])

        self.assertEqual(base.from_json_string('[{"1": 1}]'), [{"1": 1}])

        self.assertEqual(base.from_json_string('[{}]'), [{}])

        self.assertEqual(base.from_json_string('[]'), [])

        self.assertEqual(base.from_json_string('[2]'), [2])

        self.assertEqual(base.from_json_string('55'), 55)

        self.assertEqual(base.from_json_string('"aa"'), "aa")

    def test_create(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())

        self.assertEqual(r2.width, r1.width)
        self.assertEqual(r2.height, r1.height)
        self.assertEqual(r2.id, r1.id)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.y, r1.y)
