#!/usr/bin/python3
"""oooiiuuuiiooo"""
import requestssS
from sys import argv

if __name__ == "__main__":
    rqst = requests.get(argv[1])

    if rqst.status_code >= 400:
        print(f"Error code: {rqst.status_code}")
    else:
        print(rqst.content.decode())
