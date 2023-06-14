#!/usr/bin/python3
""" This module devises a function named from_json_string """

import json


def from_json_string(my_str):
    """A funtion  that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: an object

    Returns:
        an object (Python data structure)
    """

    return json.loads(my_str)
