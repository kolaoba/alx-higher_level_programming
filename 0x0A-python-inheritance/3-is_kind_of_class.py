#!/usr/bin/python3
"""
Defines a function that returns True if object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj type is an instance of, or if the object
    is an instance of a class that inherited from a_class

    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared

    Returns:
        True if object matches description
        False if otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
