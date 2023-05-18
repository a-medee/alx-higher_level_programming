#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix

    Args:
        matrix: a matrice element

    Return:
        A new matrix
    """

    if matrix is not None:
        new_matrix = matrix[:]
        k = 0
        for rows in matrix:
            new_matrix[k] = list(map(lambda x: x**2, rows))
            k += 1
        return new_matrix
