#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position

    Args:
        my_list: the list to search through
        idx: an integer representing the position
        element: the newly inserted element

    Returns:
        the original list if idx is negative or if idx is out of
        bounds, an element from my_list otherwise
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
