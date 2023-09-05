#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("{}".format(""))
    for _ in range(len(str)):
        if (ord(str[_]) >= 97 and ord(str[_]) < 97 + 26):
            print("{}".format(chr(ord(str[_]) - 32)), 
                  end="" if _ != len(str) - 1 else "\n")
        else:
            print("{}".format(str[_]), 
                  end="" if _ != len(str) - 1 else "\n")
            
uppercase("")
