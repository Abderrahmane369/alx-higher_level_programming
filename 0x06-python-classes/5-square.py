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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, _):
        if type(_) is not int:
            raise TypeError("size must be an integer")

        if _ < 0:
            raise ValueError("size must be >= 0")

        self.__size = _

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size:
            [print("#" * self.size) for _ in range(self.size)]
        else:
            print("")
