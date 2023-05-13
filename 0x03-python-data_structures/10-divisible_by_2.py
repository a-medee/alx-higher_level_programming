#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Args:
        my_list: a type list element

    Returns:
        A new list with True or False, depending on whether
        the integer at the same position in the original list is
        a multiple of 2
    """
    if not my_list:
        return None
    return [i % 2 == 0 for i in my_list]
