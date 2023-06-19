#!/usr/bin/python3

""" This module contains a class named Base """


import json


class Base:
    """This is the class Base definition

    Attributes:
        __nb_objects: TBD
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize class instances

        Args:
            id: class's objects and sub-classes' objects
        id

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json representation of list_dictionaries

        Args:
            list_dictionaries: a list of dictionaries

        Returns:
            a json representation
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of Base

        Returns:
            None
        """
        file_name = cls.__name__ + ".json"

        lis = [list_o.to_dictionary() for list_o in list_objs]
        with open(file_name, "w", encoding="utf-8") as a_file:
            json.dump(Base.to_json_string(lis), a_file)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        json_string

        Args:
            json_string: a string representing a list of dictionaries

        Returns:
            a list
        """
        return json.dumps(json_string)
