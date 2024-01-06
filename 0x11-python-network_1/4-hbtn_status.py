#!/usr/bin/python3
"""ozeàofibog"""
import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(r.content)}")
    print(f"\t- content: {r.content.decode()}")
