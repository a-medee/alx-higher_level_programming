#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary.

    Args:
        a_dictionary: a dict object
        key: the key to be deleted

    Returns:
        a dict object
    """

    if a_dictionary is not None and key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
