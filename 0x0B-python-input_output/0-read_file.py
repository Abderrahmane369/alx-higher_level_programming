#!/usr/bin/python3
"""welcome and woelc"""


def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read())
