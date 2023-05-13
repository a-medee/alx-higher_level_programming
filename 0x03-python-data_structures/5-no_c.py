#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string.

    Args:
        my_string: the string element to be parsed

    Returns:
        the newly string with no c or C characters in it
    """
    a = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            a += i
    return (a)
