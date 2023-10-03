#!/usr/bin/python3
class Rectangle():
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
