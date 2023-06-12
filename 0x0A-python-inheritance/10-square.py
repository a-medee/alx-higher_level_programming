#!/usr/bin/python3
"""This module defines a non-empty class named Rectangle
"""
import sys

sys.path.insert(1, "./9-rectangle")
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that inherites from Rectangle class

    Attributes:
        None
    """

    def __init__(self, size):
        """An initialization method for the Square class

        Args:
            size(int): the size of a Square instance

        Returns:
            None
        """
        super().__init__(size, size)
        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        """A method that helps calculate the area of this
        Square

        Args:
            None

        Returns:
            an int object
        """

        return self.__size * self.__size
