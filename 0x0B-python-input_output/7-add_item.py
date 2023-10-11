#!/usr/bin/python3
"""module"""
import sys

loadJSON = __import__('6-load_from_json_file').load_from_json_file
saveJSON = __import__('5-save_to_json_file').save_to_json_file

def main():
     l = loadJSON('add_item.json')

     for _ in sys.argv[1:]:
          l = l if type(l) is list else []
          l.append(_)

     saveJSON(l, 'add_item.json')

if __name__ == '__main__':
     main()
