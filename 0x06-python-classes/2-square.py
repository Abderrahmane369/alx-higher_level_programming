#!/usr/bin/python3
"""blblablablabla"""


class Square():
    """bla bla bla

        Attributes:
        __size (int): size.
    """
    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
