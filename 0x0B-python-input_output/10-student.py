#!/usr/bin/python3
"""azeazezaezaeaea"""


class Student():
    """zaazeazea"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            return {_: v for _, v self.__dict__.items() if _ in attrs}

        return sefl.__dict__
