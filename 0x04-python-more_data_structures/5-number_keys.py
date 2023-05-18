#!/usr/bin/python3

def number_keys(a_dictionary):
    """A function that returns the number of keys in a dictionary.

    Args:
        a_dictionary: a dictionary element

    Returns:
        an int element
    """
    key_count = 0

    for keys in a_dictionary.keys():
        key_count += 1

    return key_count
