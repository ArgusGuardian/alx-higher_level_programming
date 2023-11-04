#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for letter in my_string:
        if letter in "cC":
            continue
        new += letter
    return new
