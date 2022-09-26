#!/usr/bin/python3
"""defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): width of the new Rectangle
            height (int): height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """return the following rectangle description:
        [Rectangle] <width>/<height>
        """

        result = '[' + str(self.__class__.__name__) + '] '
        result += str(self.__width) + '/' + str(self.__height)
        return result
