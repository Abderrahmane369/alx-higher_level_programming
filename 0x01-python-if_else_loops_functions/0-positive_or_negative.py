#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number:
    if number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")
else:
    print("0 is zero")
