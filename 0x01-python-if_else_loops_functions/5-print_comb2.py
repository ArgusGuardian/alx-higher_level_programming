#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print(f"%02d" % a)
        break
    print(f"%02d" % a, end=", ")
