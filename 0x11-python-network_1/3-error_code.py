#!/usr/bin/python3
"""AAALOISA"""
import urllib.request as rqst
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with rqst.urlopen(argv[1]) as rsp:
            print(rsp.read().decode("utf-8"))
    except HTTPError as err:
        print(f"Error: {err}")
