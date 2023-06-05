#!/usr/bin/python3
"""This module defined a class named rectangle
"""


class Rectangle:
    """This is an user-defined class

    Attributes:
        None
    """
    def __init__(self, width=0, height=0):
        """The first function that is call when instanciating new objects

        Args:
            width(int): the width of the rectangle
            height(int): the width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for the width private instance attribute

        Args:
            None

        Returns:
            None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A funtion that checks the value passed to the __init__ function for
        its validity.

        Args:
            value(int): an int object

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The getter for the height private instance attribute

        Args:
            None

        Returns:
            None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A funtion that checks the value passed to the __init__ function for
        its validity.

        Args:
            value(int): an int object

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """This function returns the area of an object of type
        rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """This function returns the perimeter of an object of type
        rectangle. If width or height is equal to 0, perimeter is equal
        to 0
        """
        perim = (self.width + self.height) * 2 if self.width != 0 and \
            self.height != 0 else 0
        return perim

    def __repr__(self):
        """Returns an "informal" representation of a rectangle oject
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "<3-rectangle.Rectangle object at " + hex(id(Rectangle()))

    def __str__(self):
        """Return a formal nicely representation of a rectangle object
        """
        a = ""

        if self.width == 0 or self.height == 0:
            return a

        for i in range(self.height):
            for j in range(self.width):
                a += "#"
            if i != self.height - 1:
                a += "\n"
        return a
