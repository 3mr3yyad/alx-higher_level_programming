#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for premx in matrix:
        if len(premx) == 0:
            print()
        for x in range(len(premx)):
            print("{:d}".format(premx[x]), end="\n" if x is len(premx) - 1 else " ")
