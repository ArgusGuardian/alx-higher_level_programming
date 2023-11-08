#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lala: list(map(lambda x: x * x, lala)), matrix[:]))
