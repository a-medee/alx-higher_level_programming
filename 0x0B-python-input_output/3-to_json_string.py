#!/usr/bin/python3
import json

""" This module devises a function named to_json_string """


def to_json_string(my_obj):
    """A function that returns the JSON representation
    of an object (string):

    Args:
        my_obj: an object

    Returns:
        a json object
    """

    return json.dumps(my_obj)
