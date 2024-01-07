#!/usr/bin/python3
"""aezezaeazeae"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    bytes_content = response.text
    string = f'Body response:\n\t- type: {type(bytes_content)}\n\t- content: {bytes_content}'
    print(string)
