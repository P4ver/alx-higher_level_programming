#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    hm = []
    for g in matrix:
        p = map(lambda u: u ** 2, g)
        u = list(p)
        hm = hm + [u]
    return hm
