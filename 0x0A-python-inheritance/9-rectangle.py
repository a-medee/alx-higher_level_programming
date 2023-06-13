#!/usr/bin/python3
"""This module defines a non-empty class named Rectangle
"""
sys = __import__("sys")
sys.path.insert(1, "./7-base_geometry")
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A classe that inherits from the BaseGeometry class defined
    earlier

    Args:
        None

    Attributes:
        None
    """

    def __init__(self, width, height):
        """Class initializor, called with width and height

        Args:
            width: the rectangle instance widht
            height: the rectangle instance height

        Returns:
            None
        """
        super().__init__()

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """A method that helps calculate the area of this
        rectangle

        Args:
            None

        Returns:
            an int object
        """

        return self.__height * self.__width

    def __str__(self):
        """A function that should return a rectangle description of
        a specified scheme.

        Args:
            None

        Returns:
            a description of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """A function that prints a rectangle description of
        a specified scheme.

        Args:
            None

        Returns:
            None
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
