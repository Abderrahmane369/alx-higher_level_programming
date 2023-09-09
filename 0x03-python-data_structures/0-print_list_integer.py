#!/usr/bin/python3

def print_list_integer(my_list=[]):
    [print("{}".format(_)) for _ in my_list]

print_list_integer([5, 2, 1, 4, 6])