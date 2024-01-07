#!/usr/bin/python3
"""ozeàofibog"""
from requests import get

if __name__ == "__main__":
    r = get("https://alx-intranet.hbtn.io/status")

    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
