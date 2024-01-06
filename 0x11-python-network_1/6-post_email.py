#!/usr/bin/python3
"""oooiiuuuiiooo"""
import requests
from sys import argv

if __name__ == "__main__":
    rqst = requests.post(argv[1], data={
        "email": argv[2]
    })

    print("Your email is: {}", rqst.read())
