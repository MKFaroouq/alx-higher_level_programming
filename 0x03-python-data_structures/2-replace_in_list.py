#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0:
        return (my_list)
    elif idx > len(my_list):
        return (my_list)
    else:
        for i in my_list:
            if my_list.index(i) == idx:
                my_list[i]==new_element
            return (my_list)
