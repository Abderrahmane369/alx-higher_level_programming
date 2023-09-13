#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    for k, _ in a_dictionary.copy().items():
        if _ == value:
            a_dictionary.pop(k, None)

    return a_dictionary
