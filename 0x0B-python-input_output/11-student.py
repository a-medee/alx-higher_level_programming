#!/usr/bin/python3
""" This modules devises a classe called Student """


class Student:
    """The class Student definition

    Attributes:
        None
    """

    def __init__(self, first_name, last_name, age):
        """Student class initializator

        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that retrieves a dictionary representation of a
        Student instance

        Args:
            attrs(list): a list of strings

        Returns:
            a dictionary
        """
        str_c = int()
        a_dict = dict()

        if isinstance(attrs, list):
            for i in attrs:
                if isinstance(i, str):
                    str_c += 1
            if str_c == len(attrs):
                for i in attrs:
                    if i in self.__dict__.keys():
                        a_dict[i] = self.__dict__[i]
            else:
                a_dict = self.__dict__
        else:
            a_dict = self.__dict__

        return a_dict

    def reload_from_json(self, json):
        """A method that replaces all attributes of
        the Student instance:

        Args:
            json(dict): the first parameter

        Returns:
            None
        """
        self.__dict__ = json
