#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for number in sorted(my_list, reverse=True):
        print(number)
