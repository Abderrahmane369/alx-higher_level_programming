#!/usr/bin/python3
"""zaaaaaz"""


def pascal_triangle(n):
     """pascallllll"""
     if n <= 0:
          return []

     arr = [[1]]

     for _ in range(n - 1):
          col = [1]
          
          for n in range(1, len(arr[-1])):
               col += [arr[-1][n] + arr[-1][n - 1]]
          col += [1]
          arr += [col]

     return arr