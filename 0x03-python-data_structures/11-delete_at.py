#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list.

    Args:
        my_list: a list element to be used
        idx: the position in the list element

    Returns:
        The same list if idx is negative or out of range,
        a list element without the value at idx in the original list
    """

    if idx < 0 and idx >= len(my_list):
        return my_list

    new_list = my_list

    for i in range(0, len(new_list)):
        if i == idx:
            del new_list[i]
    return new_list
