#!/usr/bin/python3
"""This modules devises a function named is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an
    instance of, or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.

    Args:
        obj(object): the first argument
        a_class(class): the second argument

    Returns:
        Bool object
    """

    return isinstance(obj, a_class)
