#!/usr/bin/python3
"""This script defines a function that dds 2 integers"""


def add_integer(a, b=98):
    """
    adds 2 integers a and b

    Args:
        a, b - integers to be added
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return (a + b)
