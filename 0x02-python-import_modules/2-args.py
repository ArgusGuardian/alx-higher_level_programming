#!/usr/bin/python3
from sys import argv
lenght = len(argv) - 1
if lenght == 1:
    print("1 argument:")
elif lenght == 0:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(lenght))
for i in range(1, len(argv)):
    print("{:d}: {:s}".format(i, argv[i]))
