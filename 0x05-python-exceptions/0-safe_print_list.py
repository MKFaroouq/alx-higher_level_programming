#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counter = counter + 1
        except IndexError:
            continue
    print("")
    return counter
