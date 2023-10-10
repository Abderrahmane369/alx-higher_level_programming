#!/usr/bin/python3
"""looazoezaeaze"""


class BaseGeometry():
    """azeazeaea"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """azeazeaea"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator(self, "width", self.__width)
        self.integer_validator(self, "height", self.__height)
