#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys.

    Args:
        a_dictionary: a dict object

    Returns:
        None
    """

    if a_dictionary is not None:
        keys_list = sorted(a_dictionary.keys())
        for keys in keys_list:
            print(f"{keys:s}: {a_dictionary[keys]}")
