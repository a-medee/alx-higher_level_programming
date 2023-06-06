import numpy as np

def matrix_multiplication(m_a, m_b):
    """A function that multiplies 2 matrices using NumPy.

    Args:
        m_a: a matrix
        m_b: the second matrix

    Returns:
        The product of the two matrices.

    Raises:
        ValueError: If the last dimension of m_a is not the same size as the
        second-to-last dimension of m_b, if a scalar value is passed in.
    """


    return np.matmul(m_a, m_b)
