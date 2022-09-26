#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Implements sorted printing for built-in list class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
