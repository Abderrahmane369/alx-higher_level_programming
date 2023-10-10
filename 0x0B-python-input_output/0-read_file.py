#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """reads files"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())

         return f.read()