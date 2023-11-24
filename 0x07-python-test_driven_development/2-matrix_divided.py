#!/usr/bin/python3
"""A function that devides all element in a matrix"""

def matrix_divided(matrix, div):
    """Divide elements of a matrix

    Args:
        matrix: A list of lists of integers/floats
        div: The dividor

    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If matrix is not a list of lists of integers/floats
        ZeroDivisionError: If div is 0

    Returns:
        A new matrix
    """
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(ls, list) for ls in matrix)
        or not all(
            isinstance(x, (int,float))
            for x in [num for ls in matrix for num in ls]
        )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(ls) == len(matrix[0]) for ls in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(x / div, 2) for x in ls] for ls in matrix
    ]
