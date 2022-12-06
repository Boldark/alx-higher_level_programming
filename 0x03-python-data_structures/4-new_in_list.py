#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= my_list:
        retutn ("None")
    else:
        copied_list = copy_list(my_list)
        copied_list[idx] = element
        return (my_list)

def copy_list(my_list):
    copied_list = my_list
    return copied_list