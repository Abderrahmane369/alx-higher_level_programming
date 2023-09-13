#!/usr/bin/python3

def best_score(a_dictionary):
    return max(a_dictionary, key=lambda _: a_dictionary[_]) if a_dictionary != {} else None
