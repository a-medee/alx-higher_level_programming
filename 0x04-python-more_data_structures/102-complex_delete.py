#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """A function that deletes keys with a specific value in a
       dictionary.

    Args:
        a_dictionary: a dict object
        value: the value to be deleted

    Returns:
        a dict object
    """

    if a_dictionary is not None and a_dictionary and value is not None\
       and value:

        keys_values = list(tuple(a_dictionary.items()))
        if value in a_dictionary.values():
            for items in keys_values:
                if items[1] == value:
                    a_dictionary.pop(items[0])

        return a_dictionary
