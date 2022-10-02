#!/usr/bin/python3
"""Defines a Base class"""
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list(dict)): a list of dictionaries
        Returns:
            [] - If None or empty
            Otherwise - JSOn string representation of argument
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        
        Args:
            list_objs (list(instances)): list of instances who inherits of Base
                                example: list of Rectangle or Square instances
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jfile:
            if not list_objs:
                jfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of the JSON representation json_string

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instace with all attributes already set

        Args:
            **dictionary (dict): can be though of as double pointer to a dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jfile:
                list_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as cfile:
            if not list_objs or list_objs == []:
                cfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of classes instantiated from a csv file

        Returns:
            an empty list - if file does not exist
            otherwise - a list of instantiated classes
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as cfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(cfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
