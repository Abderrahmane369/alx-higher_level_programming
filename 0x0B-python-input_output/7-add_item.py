#!/usr/bin/python3
"""module"""
import sys

loadJSON = __import__('6-load_from_json_file').load_from_json_file
saveJSON = __import__('5-save_to_json_file').save_to_json_file

l = loadJSON('add_item.json')

for _ in sys.argv:
     l = l if type(l) is list else []
     l.append(_)

saveJSON(l, 'add_item.json')