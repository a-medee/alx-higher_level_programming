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
        self.set_size(size)

    def set_size(self, size):
        """A funtion that check the value passed to the __init__ function for
        its validity.

        Args:
            size(int): an int object

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
