#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    _ = 0

    while (_ < x):
        try:
            print("{:d}".format(my_list[_]), end="")
            _ = _ + 1

        except (TypeError, ValueError):
            _ = _ + 1
  
    print("{}".format(""))
    return _
