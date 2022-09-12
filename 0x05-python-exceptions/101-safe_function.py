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
        return fct(*args)
    except Exception as exception:
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
