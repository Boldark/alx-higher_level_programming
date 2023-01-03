#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_list = []

    for i in my_list:
        if i % 2 == 0:
            multiple_list.append(True)
        else:
            multiple_list.append(False)
    return (multiple_list)
