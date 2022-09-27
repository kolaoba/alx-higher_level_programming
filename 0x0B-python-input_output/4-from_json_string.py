#!/usr/bin/python3
"""Defines a function to convert JSON to Python data structure"""
import json


def from_json_string(my_str):
    """returns the Python representation of a JSON string

    Args:
        my_str (str): object to be converted to JSON
    Returns:
        object (Python data structure)
    """
    return json.loads(my_str)
