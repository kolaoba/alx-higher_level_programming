#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format()

    Arguments:
        value (any type): value to be printed

    Returns:
        bool: True if correctly printed
                Otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
