#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        u = 0
        for k in y:
            u = u + 1
            print("{:d}".format(k), end="")
            if u < 3:
                print(" ", end="")
        print("")
