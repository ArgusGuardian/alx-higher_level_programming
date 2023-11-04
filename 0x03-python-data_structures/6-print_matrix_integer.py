#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for grp in matrix:
        alert = 0
        for num in grp:
            if alert == 0:
                print("{:d}".format(num), end="")
            else:
                print(" {:d}".format(num), end="")
            alert += 1
        print()
