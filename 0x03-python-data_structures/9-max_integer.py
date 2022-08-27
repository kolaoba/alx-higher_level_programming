#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxNum = float("-inf")
    for num in my_list:
        if num > maxNum:
            maxNum = num
    return maxNum

