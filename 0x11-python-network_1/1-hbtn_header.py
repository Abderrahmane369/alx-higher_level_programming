#!/usr/bin/python3
"""loooogarithm"""
import urllib.request as rqst
from sys import argv as args

with rqst.urlopen(args[1]) as rsp:
    con = rsp

print(dict(con.getheaders()).get("X-Request-Id"))
