#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        _ = 0
        while (_ < x):
            print("{}".format(my_list[_]), end="")
            _ = _ + 1
    except Exception:
        pass
    finally:
        print("{}".format(""))
        return _
