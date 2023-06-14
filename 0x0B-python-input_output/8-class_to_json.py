#!/usr/bin/python3

""" This modules devises a function named class_to_json """

import json


def class_to_json(obj):
    """A function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: a class instance

    Returns:
        a dictionary description
    """
    return obj.__dict__
