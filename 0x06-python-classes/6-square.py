#!/usr/bin/python3
"""blblablablabla"""


class Square():
    """bla bla bla

        Attributes:
        __size (int): size.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if type(pos) is not tuple:
            raise TypeError("position must be a tuple")

        self.__position = pos

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size:
            print("\n" * self.position[1], end="")
            [
                print(" " * self.position[0] + "#" * self.size)
                for _ in range(self.size)
            ]

        else:
            print("")
