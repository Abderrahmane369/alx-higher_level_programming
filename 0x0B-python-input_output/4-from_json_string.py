#!/usr/bin/python3
"""module"""
import json


def from_json_string(my_str):
    """converts json string to python object"""
    return json.loads(my_str)
