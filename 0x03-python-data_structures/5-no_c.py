#!/usr/bin/python3
def no_c(my_string):
    remove_c = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            remove_c += x
    return (remove_c)

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))