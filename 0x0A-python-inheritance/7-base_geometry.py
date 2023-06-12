#!/usr/bin/python3
"""A module that divises an empty class named BaseGeometry.
"""


class BaseGeometry:
    """This is an user-defined geometry class

    Args:
        None

    Attributes:
        None
    """

    def area(self):
        """This is a public instance method

        Args:
            None

        Returns:
            None

        Raises:
            Exception with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates value

        Args:
            name(str): first parameter
            value(int): second parameter
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
