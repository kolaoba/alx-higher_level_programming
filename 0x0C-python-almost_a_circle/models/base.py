#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """Defines a Base class

    Attributes:
        __nb_objects (int) = number of instatiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base with instance atrribute

        Args:
            id (int): identifier of new Base
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
