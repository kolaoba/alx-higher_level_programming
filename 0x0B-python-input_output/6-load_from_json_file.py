#!/usr/bin/python3
"""Defines a function to load from JSON"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file

    Args:
        filename (str): name of json file to load
    """
    with open(filename, mode='rb') as f:
        x = json.load(f)
    return x
