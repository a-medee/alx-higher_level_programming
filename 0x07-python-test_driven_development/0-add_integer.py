#!/usr/bin/python3
""""This module implements a function to add two integers
"""


def add_integer(a, b=98):
    """A function that adds two integers together

    Args:
        a(int): first parameter
        b(int): second parameter with a default value to 98

    Returns:
        an interger

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return a + b
