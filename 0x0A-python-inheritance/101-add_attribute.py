#!/usr/bin/python3
"""This modules devises a function called add_attribute
"""


def add_attribute(obj, att_name, att_value):
    """A function that adds a new attribute to an object
    if it’s possible:

    Args:
        obj: a class object
        att_name: the attribute name to be added
        att_value: the attribute value

    Returns:
        None
    """
    if not issubclass(type(obj), (str, int, float, tuple, dict,
                                  list, set, bool)):
        if obj.__dict__ == {} or obj.__dict__:
            obj.__dict__[att_name] = att_value
    else:
        raise TypeError("can't add new attribute")
