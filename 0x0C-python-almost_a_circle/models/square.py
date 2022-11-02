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

    def update(self, *args, **kwargs):
        """Updates the square

        Args:
            args (ints): new square attributes where
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
        """
        if args and len(args) != 0:
            cnt = 0
            for arg in args:
                if cnt == 0:
                    if not arg:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif cnt == 1:
                    self.size = arg
                elif cnt == 2:
                    self.x = arg
                elif cnt == 3:
                    self.y = arg
                cnt += 1

        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == "id":
                    if not arg:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif key == "size":
                    self.size = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>
        """
        result = f"[Square] ({self.id}) {self.x}/{self.y} - "
        result += f"{self.size}"
        return result
