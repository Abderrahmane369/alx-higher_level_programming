#!/usr/bin/python3

def weight_average(my_list=[]):
    sum = 0
    d = 0
    
    if my_list == []:
        return 0

    for _ in my_list:
        sum += _[0] * _[1]
        d += _[1]

    return sum / d
