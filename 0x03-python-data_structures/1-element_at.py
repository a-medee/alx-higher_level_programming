#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: the list to search through
        idx: the index at which the element lied

    Return:
        element at idx in my_list if idx is negative or
        out of range, the actual element otherwise
    """

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
