#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for _ in matrix:
        [print("{:d}".format(__), end=" " if __ != len(_) - 1 else "\n") for __ in _]
