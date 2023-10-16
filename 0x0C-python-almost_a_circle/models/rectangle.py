#!/usr/bin/python3
"""No modules"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")

        if type(self.__x) is not int:
            raise TypeError("x must be an integer")

        if type(self.__y) is not int:
            raise TypeError("y must be an integer")

        if self.__width <= 0:
            raise ValueError("width must be > 0")

        if self.__height <= 0:
            raise ValueError("height must be > 0")

        if self.__x < 0:
            raise ValueError("x must be >= 0")

        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")

        if w <= 0:
            raise ValueError("width must be > 0")

        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("width must be an integer")

        if h <= 0:
            raise ValueError("height must be > 0")

        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, _x):
        if type(_x) is not int:
            raise TypeError("width must be an integer")

        if _x < 0:
            raise ValueError("x must be >= 0")

        self.__x = _x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, _y):
        if type(_y) is not int:
            raise TypeError("width must be an integer")

        if _y < 0:
            raise ValueError("y must be >= 0")

        self.__y = _y

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y + (" " * self.x + "#" *
              self.width + "\n") * self.height, end="")

    def to_dictionary(self):
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x,
            self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for _, arg in enumerate(args):
                if _ == 0:
                    self.id = arg
                if _ == 1:
                    self.width = arg
                if _ == 2:
                    self.height = arg
                if _ == 3:
                    self.x = arg
                if _ == 4:
                    self.y = arg
        else:
            for k, _ in kwargs.items():
                if hasattr(self, k):
                    if k == "width":
                        self.width = _
                    if k == "height":
                        self.height = _
                    if k == "x":
                        self.x = _
                    if k == "y":
                        self.y = _
                    if k == "id":
                        self.id = _
