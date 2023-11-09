#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x_a: list(map(lambda g: g**2, x_a)), matrix))
