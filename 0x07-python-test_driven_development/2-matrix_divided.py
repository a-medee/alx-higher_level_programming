#!/usr/bin/python3
"""This module designed a function named matrix_divided
   that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix.

    Args:
        matrix: a list of list of ints of floats objects
        div(int): second parameter

    Returns:
        A new matrix

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of intege
    rs/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    type_list = [int, float]

    if type(matrix) is list:
        for i in matrix:
            if type(i) is not list:
                msg = "matrix must be a matrix (list of lists) of"
                raise TypeError(msg + " integers/floats")
            if len(i) != len(matrix[0]):
                msg = "Each row of the matrix must have the"
                raise TypeError(msg + " same size")
            for k in i:
                if type(k) not in type_list:
                    msg = "matrix must be a matrix (list of lists)"
                    raise TypeError(msg + " of integers/float")
    else:
        msg = "matrix must be a matrix (list of lists) of"
        raise TypeError(msg + " integers/floats")

    if type(div) not in type_list:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)),
                    matrix))
