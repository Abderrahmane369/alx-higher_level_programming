#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for _ in matrix:
        [print("{:d}".format(__), end=" ") for __ in _]
        print("{}".format("\n"))
