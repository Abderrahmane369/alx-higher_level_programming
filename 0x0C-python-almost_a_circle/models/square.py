#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """azeazeaeazea"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """azeazeaeazea"""
        return self.width
    
    @size.setter
    def size(self, _):
        """azeazeaeazea"""
        self.width = _
        self.height = _

        if _ <= 0:
            raise ValueError("width must be > 0")
    
    def update(self, *args, **kwargs):
        """azeazeaeazea"""
        if len(args) > 0:
            for _, arg in enumerate(args):
                if _ == 0:
                    self.id = arg
                if _ == 1:
                    self.size = arg
                if _ == 2:
                    self.x = arg
                if _ == 3:
                    self.y = arg
        else:
            for k, _ in kwargs.items():
                if hasattr(self, k):
                    if k == "size":
                        self.size = _
                    if k == "x":
                        self.x = _
                    if k == "y":
                        self.y = _
                    if k == "id":
                        self.id = _

    def to_dictionary(self):
        """azeazeaeazea"""
        return {
            'x': self.x,
            'y': self.y,
            'size': self.size,
            'id': self.id
        }

    def __str__(self):
        """azeazeaeazea"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)