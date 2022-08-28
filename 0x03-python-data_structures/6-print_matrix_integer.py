#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j, col in enumerate(row):
            print("{:d}".format(col), end="")
            if j != len(row) - 1:
                print(" ", end="")
        print("")
