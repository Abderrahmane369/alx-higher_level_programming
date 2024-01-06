#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request as rq

with rq.urlopen("https://alx-intranet.hbtn.io/status") as rp:
    cnt = rp.read()


print('Body response:')
print(f'\t- type: {type(cnt)}')
print(f'\t- content: {cnt}')
print(f'\t- utf8 content: {cnt.decode("utf-8")}')
