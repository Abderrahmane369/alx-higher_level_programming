#!/usr/bin/python3
"""this is"""


def matrix_divided(matrix, div):
    """and imagine dragon"""
    f = frozenset
    m = matrix

    if type(matrix) is not list or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    for _ in matrix:
        if type(_) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

        for __ in _:
            if type(__) not in {int, float}:
                raise TypeError(
                    "matrix must be a matrix" +
                    "(list of lists) of integers/floats"
                    )

    if len({len(r) for r in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in {int, float}:
        raise TypeError("div must be a number")

    if not div:
        raise ZeroDivisionError("division by zero")

    return [[round(float(_ / div), 2) for _ in r] for r in matrix]
