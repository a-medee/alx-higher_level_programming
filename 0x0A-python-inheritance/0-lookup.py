#!/usr/bin/python3
"""This module devises a function named lookup
"""


def lookup(obj):
    """A funtion that returns the list of available attributes
    and methods of an object:

    Args:
        obj(object): a type object object

    Returns:
        a list object
    """

    return dir(obj)
