#!/usr/bin/python3
""" This module devises a function named save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: the object to save into filename
        filename: the name stands for itself

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file, ensure_ascii=False)
