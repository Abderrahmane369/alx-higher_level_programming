#!/usr/bin/python3
"""Module documentation"""


def lookup(obj):
     """
     return list of available attributes

     Parameters:
       -obj: object

     Returns:
      -list: list of attributes
      """

     return dir(obj)
