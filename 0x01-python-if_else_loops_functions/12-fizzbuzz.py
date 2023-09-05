#!/usr/bin/python3
def fizzbuzz():
    for _ in range(1, 101):
        if _ % 3 == _ % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif not _ % 3:
            print("{}".format("Fizz"), end=" ")
        elif not _ % 5:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(_), end=" ")
