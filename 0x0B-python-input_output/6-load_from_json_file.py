#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """loads from json file"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())

