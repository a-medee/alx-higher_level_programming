#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list

    Args:
        my_list: a list object
        x: represents the number of elements to print

    Returns:
        the real number of elements printed
    """
    nbr = 0
    try:
        if my_list is not None and my_list:
            for i in range(x):
                print(my_list[i], end="")
                nbr += 1
    except IndexError:
        pass
    print()
    return nbr
