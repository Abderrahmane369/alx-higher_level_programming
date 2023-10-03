#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h
