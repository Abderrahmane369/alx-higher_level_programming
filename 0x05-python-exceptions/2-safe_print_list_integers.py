#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    v = 0

    for _ in range(0, x):
        try:
            print("{:d}".format(my_list[_]), end="")
            v = v + 1

        except (ValueError, TypeError):
            pass

    print("{}".format(""))
    return v

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))