#!/usr/bin/python3
"""looazoezaeaze"""


class BaseGeometry():
    """azeazeaea"""
    def area(self):
<<<<<<< HEAD
        raise Exception("area() is not implemented")*

=======
        raise Exception("area() is not implemented")
         
>>>>>>> 336b3c340ac6f162ea3d193a4a6c508db1a20ebc
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
