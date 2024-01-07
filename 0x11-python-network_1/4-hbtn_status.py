#!/usr/bin/python3
"""aezezaeazeae"""
from requests import get

if __name__ == "__main__":
    response = get('https://intranet.hbtn.io/status')
    bytes_content = response.text
    string = f'Body response:\n\t- type: {type(bytes_content)}\n\t- content: {bytes_content}'
    print(string)
