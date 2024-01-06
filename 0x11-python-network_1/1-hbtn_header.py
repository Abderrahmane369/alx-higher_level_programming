#!/usr/bin/python3
"""loooogarithm"""
import urllib.request as rqst
import sys

with rqst.urlopen(sys.argv[1]) as rsp:
    con = dict(rsp.getheaders())

print(con.get("X-Request-Id"))
