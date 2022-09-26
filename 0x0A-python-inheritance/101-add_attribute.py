#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """add a new attribute to an object (if possible)

    Args:
        obj (any): object to add an attribute to
        attr (str): attribute to add to obj
        value (any): value of attr
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
