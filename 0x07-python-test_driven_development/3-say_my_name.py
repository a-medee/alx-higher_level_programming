#!/usr/bin/python3
""" This modules defines one funtion for a name call
"""

def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>

    Args:
        first_name(str): first parameter
        last_name(str): second parameter

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
