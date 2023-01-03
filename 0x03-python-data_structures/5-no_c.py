#!/usr/bin/python3
def no_c(my_string):
    remove_c = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            remove_c += x
    return (remove_c)
