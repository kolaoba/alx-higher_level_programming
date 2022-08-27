#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for l in my_string:
        if l not in 'cC':
            new_string.append(l)
    return ''.join(new_string)
