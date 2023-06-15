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

    def to_json(self):
        """A method that retrieves a dictionary representation of a
        Student instance

        Args:
            None

        Returns:
            None
        """
        return self.__dict__
