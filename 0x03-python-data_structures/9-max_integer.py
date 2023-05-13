#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list.

    Args:
        my_list: a list element

    Returns:
        the biggest int from my_list, None if my_list is empty
    """

    if my_list:
        value = my_list[0]

        for i in my_list:
            if i > value:
                value = i
        return value
    return None
