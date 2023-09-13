#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if _ == search else _ for _ in my_list]
