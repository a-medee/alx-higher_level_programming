#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position
       without modifying the original

    Args:
        my_list: the list to be processed
        idx: an integer type, where an element resides in the list
        element: the newly element to be inserted

    Returns:
        the copy of the original list if idx isn't valid for the list,
        the list with element (the 3rd parameter for this function)
        inserted otherwise
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:]
    new_list[idx] = element

    return new_list
