#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        denom = 0
        for x in my_list:
            num += (x[0] * x[1])
            denom += (x[1])
        return (num/denom)
    return 0
