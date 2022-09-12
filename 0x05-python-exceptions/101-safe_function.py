#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    executes a function safely

    Args:
        fct (function): function to be executed
        *args :arguments for the function fct
 
    Returns:
        the result(s) of the function
    """
    try:
        res = fct(*args)
        return res
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
