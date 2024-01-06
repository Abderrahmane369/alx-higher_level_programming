#!/usr/bin/python3
"""oooiiuuuiiooo"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    rqst = requests.post("http://0.0.0.0:5000/search_user", data={
        "q": argv[1] if len(argv) == 2 else ""
    })

    try:
        if json.loads(rqst.content.decode()) == {}:
            print("No result")

        else:
            print("[{}] {}".format(
                json.loads(rqst.content.decode()).get('id'),
                json.loads(rqst.content.decode()).get('name')
            ))
    except ValueError:
        print("Not a valid JSON")
