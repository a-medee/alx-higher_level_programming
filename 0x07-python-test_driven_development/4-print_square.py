#!/usr/bin/python3
"""This module devises one function named print_square
   which takes in a integer for parameters
"""


def print_square(size):
    """A function that prints a square with the character #

    Args:
        size(int): the size length of the square

    Returns:
        None

    Raises:
        TypeError if text is not a string
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    k = 0
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
