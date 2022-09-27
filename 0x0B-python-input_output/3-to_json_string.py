#!/usr/bin/python3
"""Defines a function to convert string to JSON"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)
    """
    return json.dumps(my_obj)
