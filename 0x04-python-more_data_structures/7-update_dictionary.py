#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """A function that replaces or adds key/value in a dictionary.
        If a key exists in the dictionary, the value will be replaced
        If a key doesn’t exist in the dictionary, it will be created

    Args:
        a_dictionnary: a dictionnary element
        key: a string object to be added
        value: a value of any type to be attached to the key whose is to
        be added

    Returns:
        a dict object
    """

    if a_dictionary is not None:
        keys_list = list(a_dictionary.keys())

        if key is not None or value is not None:
            for keys in keys_list:
                if key == keys:
                    a_dictionary[keys] = value
                else:
                    a_dictionary[key] = value

        return a_dictionary
