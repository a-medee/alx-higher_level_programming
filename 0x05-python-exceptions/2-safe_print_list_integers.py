#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of
    a list and only integers.

    Args:
        my_list: a list object
        x: an int element, represents the number of element to access

    Return:
        the real number of integers printed
    """
    nbr = 0

    if my_list is not None and my_list:

        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                nbr += 1
            except ValueError:
                pass
            except TypeError:
                pass
    print()
    return nbr
