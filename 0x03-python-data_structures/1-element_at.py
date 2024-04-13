#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for idx in my_list:
            if my_list.index(idx):
                print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
                return idx
