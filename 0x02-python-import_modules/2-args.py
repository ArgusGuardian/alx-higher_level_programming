#!/usr/bin/python3
import sys
len = len(sys.argv) - 1
if len == 1:
    print("1 argument:")
elif len == 0:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(len))
for i in range(1, len(sys.argv)):
    print("{:d}: {:s}".format(i, sys.argv[i]))
