#!/usr/bin/python3
"""oooiiuuuiiooo"""
import requests
from sys import argv

if __name__ == "__main__":
    rqst = requests.post("http://0.0.0.0:5000/search_user", data={
        "q": argv[1] if len(argv) == 2 else ""
    })

    try:
        if rqst.json() == {}:
            print("No result")

        else:
            print("[{}] {}".format(
                rqst.json().get('id'),
                rqst.json().get('name')
            ))
    except ValueError:
        print("Not a valid JSON")
