#!/usr/bin/python3
for _ in range(26):
    print("{}".format(chr((122 - 90) * ((_ + 1) % 2) + 90 - _)), end="")
