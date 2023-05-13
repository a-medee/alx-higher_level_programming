#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order

    Args:
        my_list: a list element whose value is to be printed

    Return:
        None
    """
    list_size = len(my_list) - 1
    for i in range(list_size, -1, -1):
        print("{:d}".format(my_list[i]))
