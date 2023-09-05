#!/usr/bin/python3
for _ in range(100):
    if _ % 11 != 0 and (_ % 10) * 10 > _:
        print("{:02}".format(_), end=", " if _ != 89 else "\n")
