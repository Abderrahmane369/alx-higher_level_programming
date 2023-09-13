#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for _, val in sorted(a_dictionary.items()):
        print("{}: {}".format(_, val))
