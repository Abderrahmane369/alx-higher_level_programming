#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format(""))
        return

    for _ in matrix:
        [print("{:d}".format(__), 
               end=" " if __ != _[-1] else "\n") for __ in _]
