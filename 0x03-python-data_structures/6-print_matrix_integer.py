#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix: the matrix to be printed

    Returns:
        None
    """
    for i in matrix:
        if not i:
            print("")
            return
        for j, k in enumerate(i):
            if j != len(i) - 1:
                print("{:d}".format(k), end=" ")
            else:
                print("{:d}".format(k))
