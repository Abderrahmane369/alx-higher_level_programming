#!/usr/bin/python3
"""GITHUBIZATON"""
import requests
from sys import argv

if __name__ == "__main__":
    rqst = requests.get("https://api.github.com/user",
                        auth=(argv[1], argv[2]))
    print(rqst.json().get('id'))
