#!/usr/bin/python3
"""
Defines a function that returns True if object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    returns True if obj type is exactly same as a_class

    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared

    Returns:
        True if object is exactly an instance of specified class
        False if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
