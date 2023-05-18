#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of different elements in two sets.

    Args:
        set_1: the first set
        set_2: the second set

    Returns:
        a set element containing different elements in set_1 and set_2
    """
    if set_1 is not None and set_2 is not None:
        return (set_1 | set_2) - set_1.intersection(set_2)
