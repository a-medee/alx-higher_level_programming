#!/usr/bin/python3
"""
    This is an user-define Square
"""


class Square:
    """A user-define square

    Attributes:
        None
    """

    def __init__(self, size=0):
        """The first function that is call when instanciating new objects

        Args:
            size(int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """The getter for the size private instance attribute

        Args:
            None

        Returns:
            None
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A funtion that checks the value passed to the __init__ function for
        its validity.

        Args:
            value(int): an int object

        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A function that returns the current area of a Square type

        Args:
            None

        Returns:
            None
        """
        return self.__size**2
