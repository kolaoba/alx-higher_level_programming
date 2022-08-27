#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all characters c and C from a string
    """
    new_string = [l for l in my_string if l != 'c' and l !='C']
    return "".join(new_string)
