#!/usr/bin/python3

def weight_average(my_list=[]):
    """A function that returns the weighted average of all
       integers tuple

    Args:
        my_list: a list object

    Returns:
        a number
    """

    if not my_list:
        return 0

    mult = 0
    somm = 0
    for values in my_list:
        if values and len(values) >= 2 and values is not None:
            mult += values[0] * values[1]
            somm += values[1]

    return mult / somm
