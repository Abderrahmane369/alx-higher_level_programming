#!/usr/bin/python3
"""aezezaeazeae"""
from requests import get

if __name__ == "__main__":
    response = get('https://intranet.hbtn.io/status')
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
        type(bytes_content), bytes_content)
    print(string)
