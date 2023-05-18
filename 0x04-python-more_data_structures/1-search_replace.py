#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.

    Args:
        my_list: a list element
        search: an element to look for
        replace: the new element to place in the list

    Returns:
        The newly created list
    """

    if my_list is not None:
        new_list = []
        for i in my_list:
            if i != search:
                new_list.append(i)
            else:
                new_list.append(replace)
        return new_list
