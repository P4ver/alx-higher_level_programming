#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for y in matrix:
            u = 0
            for k in y:
                u = u + 1
                if u == 1:
                    print("{:d}".format(k), end="")
                else:
                    print(" {:d}".format(k), end="")
            print("")
