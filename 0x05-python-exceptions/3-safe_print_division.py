#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints the result

    Arguments:
        a, b (int): numbers to be divided

    Returns:
        the value of the division, otherwise None
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
