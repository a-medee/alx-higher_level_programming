#!/usr/bin/python3

def safe_print_integer(value):
    """A function that prints function that prints an integer
       with "{:d}".format(), a list and only integers.

    Args:
       value: can be of any type

    Return:
        True if value has been correctly printed (it means the value
        is an integer)
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    except TypeError:
        return False
    return True
