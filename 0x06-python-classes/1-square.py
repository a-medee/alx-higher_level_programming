#!/usr/bin/python3
"""
    This is an user-define Square
"""


class Square:
    """A user-define square

    Attributes:
        None
    """

    def __init__(self, size):
        """The first function that is call when instanciating new objects

        Args:
            size(int): the size of the square
        """
        self.__size = size
