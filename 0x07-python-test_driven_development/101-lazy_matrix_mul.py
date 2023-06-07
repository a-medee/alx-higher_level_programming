#!/usr/bin/python3
import numpy as np

"""This module devises one function named
   to mutiply two matrices
"""


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices

    Args:
        m_a: a matrix
        m_b: the second matrix

    Returns:
        None

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be
    multiplied.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for elt in m_a:
        for el in elt:
            if type(el) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for elt in m_b:
        for el in elt:
            if type(el) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for elt in m_a:
        if len(elt) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for elt in m_b:
        if len(elt) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
