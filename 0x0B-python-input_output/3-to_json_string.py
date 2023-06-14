#!/usr/bin/python3
""" This module devises a function named to_json_string """

json = __import__("json")


def to_json_string(my_obj):
    """A function that returns the JSON representation
    of an object (string):

    Args:
        my_obj: an object

    Returns:
        a json object
    """

    return json.dumps(my_obj)
