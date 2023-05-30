#!/usr/bin/python3

def safe_print_division(a, b):
    """A function that divides 2 integers and prints the result.

    Args:
        a: an int object
        b: an int object

    Return:
        the value of the division, otherwise: None
    """
    res = None

    try:
        res = a / b
    except BaseException:
        pass
    finally:
        if res is not None:
            print("Inside result: {:.1f}".format(res))
        else:
            print("Inside result: {}".format(None))
    return res
