#!/usr/bin/python3
"""AAALOISA"""
import urllib.request as rqst
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    parsedData = parse.urlencode({
        "email": argv[2]
    }).encode()

    with rqst.urlopen(rqst.Request(argv[1],
                                   data=parsedData, method="POST")) as rsp:
        print(rsp.read().decode())
