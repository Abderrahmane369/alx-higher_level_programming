#!/usr/bin/python3
"""wooooooow"""


class Rectangle():
    """wooooooow"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width * self.height:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        if not self.width * self.height:
            return ""

        return ("#" * self.width + "\n") * (self.height - 1) + "#" * self.width
