#!/usr/bin/python3

""" This modules devises a class named Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is a special kind of rectangle where all
    sides have equal length.

    Attributes:
        None
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of the square

        Args:
            size: The new size of the square
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")

        self.width = size
        self.height = size

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
            if len(args) == 4:
                self.id, self.size, self.x, self.y = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 1:
                self.id = args[0]

        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
                    elif key == "id":
                        self.id = value

    def to_dictionary(self):
        """Returns a dictionary representation of a a square.

        Returns:
            dict: A dictionary representation of a square
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
