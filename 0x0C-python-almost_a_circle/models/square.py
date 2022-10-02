#!/usr/bin/python3
"""Defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes square class

        Args:
            size (int): length of side of new square
            x (int): x-coordinate of square
            y (int): y-coordinate of sqaure
            id (int): identifier for instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
