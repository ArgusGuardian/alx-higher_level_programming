#!/usr/bin/python3
import sys
len = len(sys.argv) - 1
if len == 1:
    print("1 argument:")
elif len == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(len))
counter = 0
for arg in sys.argv[1:]:
    counter += 1
    print("{}: {}".format(counter, arg))
