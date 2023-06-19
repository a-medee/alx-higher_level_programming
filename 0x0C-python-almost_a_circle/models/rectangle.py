#!/usr/bin/python3

""" This module devises a class named Rectangle """

from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class definition.
    It inherits from the Base class

    Attributes:
        None
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle.
            y: The y-coordinate of the rectangle.
            id: The ID of the rectangle.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle.

        Args:
            width: The new width of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle.

        Args:
            height: The new height of the rectangle.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x-coordinate of the rectangle.

        Args:
            x: The new x-coordinate of the rectangle.
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y-coordinate of the rectangle.

        Args:
            y: The new y-coordinate of the rectangle.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the area of a rectangle

        Args:
            None

        Returns:
            int: the area
        """
        return self.height * self.width

    def display(self):
        """Print in stdout the rectangle with #

        Args:
            None

        Returns:
            None
        """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for l in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """A function that returns a string representation of Rectangle

        Args:
            None

        Returns:
            a string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assign an argument to each instance attribute

        Args:
            args: a tuple containing the attribute to
        assign
            kwargs: a double pointer to a dictionary: key/value

        Returns:
            None
        """
        if args and len(args) != 0:
            if len(args) == 5:
                self.id, self.width, self.height, self.x, self.y = args
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args
            elif len(args) == 3:
                self.id, self.width, self.height = args
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 1:
                self.id = args[0]

        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
                    elif key == "id":
                        self.id = value

    def to_dictionary(self):
        """Returns a dictionary representation of a rectangle.

        Returns:
            dict: A dictionary representation of a rectangle.
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
