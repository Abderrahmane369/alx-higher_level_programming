#!/usr/bin/python3
"""loooogarithm"""
import urllib.request as rqst
import sys

with rqst.urlopen(sys.argv[1]) as rsp:
    con = rsp

print(dict(con.getheaders()).get("X-Request-Id"))
