#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    arr = []
    for _ in range(list_length):
        try:
            c = my_list_1[_] / my_list_2[_]

        except TypeError:
            c = 0
            print("{}".format("wrong type"))

        except ZeroDivisionError:
            c = 0
            print("{}".format("division by 0"))

        except IndexError:
            c = 0
            print("{}".format("out of range"))

        finally:
            arr.append(c)

    return arr
