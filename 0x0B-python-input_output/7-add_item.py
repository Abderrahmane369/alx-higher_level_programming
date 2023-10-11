#!/usr/bin/python3
"""module"""
import sys

loadJSON = __import__('6-load_from_json_file').load_from_json_file
saveJSON = __import__('5-save_to_json_file').save_to_json_file

try:
     loaded = loadJSON('add_item.json')
except json.decoder.JSONDecodeError:
     loaded = []

loaded += [sys.argv[1:]]

saveJSON(l, 'add_item.json')
