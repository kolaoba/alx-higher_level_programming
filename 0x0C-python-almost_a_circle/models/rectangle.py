#!/usr/bin/python3
"""Defines a Rectangle class which inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle Class ineriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new rectangle with attributes

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-axis coordinate
            y (int): y-axis coordinate
            id (int): class identifier inherited from Base
        Raises:
            TypeError: if either of width, height, x or y is not an int
            ValueError: if either of width, height, x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the new Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the new Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the new Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the y coordinate of the new Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
