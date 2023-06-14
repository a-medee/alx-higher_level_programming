#!/usr/bin/python3

""" This module defines a function named pascal_triangle """

def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n: the first parameter

    Returns:
        a list of lists, an empty list if n <=0
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
