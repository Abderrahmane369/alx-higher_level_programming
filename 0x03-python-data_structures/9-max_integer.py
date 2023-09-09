#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    c = my_list[0]

    for _ in my_list:
        if _ > c:
            c = _

    return c
