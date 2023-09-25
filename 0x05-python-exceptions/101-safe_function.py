#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)

    except Exception as _e:
        print("Exception: {}".format(_e), file=stderr)

        return None
