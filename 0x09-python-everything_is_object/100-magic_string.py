#!/usr/bin/python3
def magic_string():
    global iter
    iter += 1
    return "BestSchool" * iter + ',' * (iter - 1)