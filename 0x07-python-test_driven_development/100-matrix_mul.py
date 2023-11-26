#!/usr/bin/python3
"""Function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Perform matrix multiplication.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Raises:
        TypeError: If inputs are not lists, or if elements are not integers or floats.
        ValueError: If matrices are empty or incompatible for multiplication.

    Returns:
        list: The result of matrix multiplication as a list of lists.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(e, list) for e in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(e, list) for e in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(e, (float, int)) for row in m_a for e in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(e, (float, int)) for row in m_b for e in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(e) == len(m_a[0]) for e in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(e) == len(m_b[0]) for e in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not len(m_b) == len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    m_mul = [[0 for e in range(len(m_b[0]))] for e in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_mul[i][j] += m_a[i][k] * m_b[k][j]

    return m_mul
