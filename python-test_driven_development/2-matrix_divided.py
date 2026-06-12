#!/usr/bin/python3
"""This module divides all elements of a matrix.

It checks that the matrix is valid.
It checks that all rows have the same size.
It returns a new matrix with divided values.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    Each result is rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        for number in row:
            if type(number) not in (int, float):
                raise TypeError(msg)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in row] for row in matrix]
