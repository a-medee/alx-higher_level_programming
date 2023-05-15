#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds two tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        a tuple resulting from the addition of tuple_a and tuple_b
    """
    size_tuple_a = len(tuple_a)
    size_tuple_b = len(tuple_b)

    if size_tuple_a == 0:
        if size_tuple_b == 0:
            return 0 + 0, 0 + 0
        if size_tuple_b == 1:
            return 0 + tuple_b[0], 0 + 0
        if size_tuple_b >= 2:
            return 0 + tuple_b[0], 0 + tuple_b[1]

    elif size_tuple_a == 1:
        if size_tuple_b == 0:
            return tuple_a[0] + 0, 0 + 0
        if size_tuple_b == 1:
            return tuple_a[0] + tuple_b[0], 0 + 0
        if size_tuple_b >= 2:
            return tuple_a[0] + tuple_b[0], 0 + tuple_b[1]

    else:
        if size_tuple_b == 0:
            return tuple_a[0] + 0, tuple_a[1] + 0
        if size_tuple_b == 1:
            return tuple_a[0] + tuple_b[0], tuple_a[1] + 0
        if size_tuple_b >= 2:
            return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
