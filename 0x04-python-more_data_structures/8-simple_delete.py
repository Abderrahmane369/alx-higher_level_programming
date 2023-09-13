#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    dict = a_dictionary
    dict.pop(key, None)

    return dict
