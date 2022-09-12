#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    prints an integer safely
    prints message to standard error if ValueError is caught

    Arguments:
        value (int): integer to be printed

    Returns:
        False - if TypeError or ValueError occurs
        True - otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
