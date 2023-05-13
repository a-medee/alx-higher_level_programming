#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints integers from a list

    Args:
        my_list: the list whose elements is to be printed

    Returns:
        None
    """

    for i in my_list:
        print("{:d}".format(i))
