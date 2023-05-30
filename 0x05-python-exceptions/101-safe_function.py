#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """A function that executes a function safely.

    Args:
        fct: a pointer to a function
        args: a tuple of args to be passed to fct

    Returns:
         the result of the function fct
    """

    r = None
    try:
        r = fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return r
