#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    i = 0
    if roman_string:
        while i < len(roman_string):
            if i < len(roman_string) - 1 and roman_string[i] == 'I' and roman_string[i+1] in "MDCLXV":
                number += roman_helper(roman_string[i+1]) - 1
                i += 2
            else:
                number += roman_helper(roman_string[i])
                i += 1
    return number


def roman_helper(letter):
    number = 0
    if letter == 'M':
        number += 1000
    elif letter == 'D':
        number += 500
    elif letter == 'C':
        number += 100
    elif letter == 'L':
        number += 50
    elif letter == 'X':
        number += 10
    elif letter == 'V':
        number += 5
    elif letter == 'I':
        number += 1
    return number
