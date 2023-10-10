#!/usr/bin/python3
"""looazoezaeaze"""


class BaseGeometry():
    """azeazeaea"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        BaseGeometry.integer_validator(self, "width", self.width)
        BaseGeometry.integer_validator(self, "height", self.height)

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
