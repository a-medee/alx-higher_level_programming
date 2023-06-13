#!/usr/bin/python3
"""This module defines a non-empty class named Rectangle
"""
sys = __import__("sys")
sys.path.insert(1, "./7-base_geometry")
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A classe that inherits from the BaseGeometry class defined
    earlier

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

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is zero or negative
        """
        super().__init__()

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
