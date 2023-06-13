#!/usr/bin/python3
"""A module that divises an empty class named BaseGeometry.
"""


class BaseGeometry:
    """This is an user-defined geometry class

    Attributes:
        None

    Raises:
        Exception: with the message area() is not implemented
    """

    def area(self):
        """This is a public instance method

        Args:
            None

        Returns:
            None

        Raises:
            Exception: with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates value

        Args:
            name(str): first parameter
            value(int): second parameter

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is zero or negative
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
