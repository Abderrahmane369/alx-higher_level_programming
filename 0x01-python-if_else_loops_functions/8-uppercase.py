#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("{}".format(""))
        return
    for _ in range(len(str)):
        print("{}".format(chr(ord(str[_]) - 32)
                            if ord(str[_]) >= 97 and ord(str[_]) < 97 + 26
                            else str[_]),
                end="" if _ != len(str) - 1 else "\n")
