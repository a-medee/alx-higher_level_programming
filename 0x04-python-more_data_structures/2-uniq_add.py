#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer).

    Args:
        my_list: a list element

    Returns:
        an int element
    """

    if my_list is None:
        return None

    new_list = my_list[:]

    new_list.sort()

    another = []
    for i in new_list:
        if i not in another:
            another.append(i)
    return sum(another)
