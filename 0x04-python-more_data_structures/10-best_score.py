#!/usr/bin/python3

def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value.

    Args:
        a_dictionary: a dict object

    Returns
        an int object
    """

    if a_dictionary is None:
        return None

    values_list = max(list(a_dictionary.values()))

    for i, j in a_dictionary.items():
        if j == values_list:
            return i
