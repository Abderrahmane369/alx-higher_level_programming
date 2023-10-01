#!/usr/bin/python3
"""loooooazeozaelzeal"""


def print_square(size):
    """mazemlzaeoolsd"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for _ in range(size)]
