#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    factor = 1
    for row in my_list:
        for i in row:
            factor *= i
        x += factor
        factor = 1
    y = 0
    for row in my_list:
        y += row[-1]
    return x / y
