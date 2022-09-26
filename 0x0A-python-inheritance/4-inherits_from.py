#!/usr/bin/python3
"""
Defines a function that returns True if object is an instance of
a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    returns True if obj type is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared

    Returns:
        True if object matches description
        False if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
