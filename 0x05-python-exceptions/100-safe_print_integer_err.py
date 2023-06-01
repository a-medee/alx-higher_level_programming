#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """A function that prints an integer.

    Args:
        value: an int object

    Returns:
        True if value has been correctly printed (
        it means the value is an integer)
    """
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
