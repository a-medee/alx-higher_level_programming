#!/usr/bin/python3
"""A module that divises an empty class named BaseGeometry.
"""


class BaseGeometry:
    """This is an user-defined geometry class

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
