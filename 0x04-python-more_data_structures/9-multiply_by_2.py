#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values
       multiplied by 2

    Args:
        a_dictionary: a dict object

    Returns:
        a new dictionary
    """

    if a_dictionary is not None:
        new_dict = dict()
        for keys, values in a_dictionary.items():
            new_dict[keys] = 2 * values
        return new_dict
