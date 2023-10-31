#!/usr/bin/python3
def uppercase(str):
    string = ""
    for letter in str:
        if ord(letter) > 90:
            letter = chr(ord(letter) - 32)
        string += letter
    print("{:s}".format(string))
