#!/usr/bin/python3
"""A module that divises a class named MyInt
"""


class MyInt(int):
    """This is the definition of MyInt class
    It inherits the int class

    MyInt is a rebel. MyInt has == and != operators inverted

    Attributes:
        None
    """

    def __init__(self, an_int):
        """The method that initializes an object of type
        MyInt

        Args:
            an_int(int): the parameter

        Returns:
            None
        """
        super().__init__()

    def __eq__(self, __value):
        """A funtion that executes the != operator
        on an object of the class MyInt

        Args:
            value: an int object

        Returns:
            a bool object
        """
        return super().__ne__(__value)

    def __ne__(self, __value):
        """A funtion that executes the == operator
        on an object of the class MyInt

        Args:
            value: an int object

        Returns:
            a bool object
        """

        return super().__eq__(__value)
