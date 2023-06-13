#!/usr/bin/python3

""" This modules defined a function named load_from_json_file"""


import json


def load_from_json_file(filename):
    """A  function that creates an Object from a “JSON file”

    Args:
        filename: path to the file to be used filename

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        json.load(a_file)
