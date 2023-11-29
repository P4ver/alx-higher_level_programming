#!/usr/bin/python3
"""Module 2-matrix_divided,"""


def matrix_divided(matrix, div):
    """
    Divide two nm.

    Args:
        matrix: matrix (list of lists),
        div: num to divide,
    Returns:
        list: list divided by div.
    Raises:
        TypeError: if they aren't int or float
        ZeroDivisionError: if the div is zero.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (
        isinstance(matrix, list) and
        all(type(rw) is list for rw in matrix) and
        all(type(el) in (int, float) for q in matrix for el in q)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(q / div, 2) for q in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
