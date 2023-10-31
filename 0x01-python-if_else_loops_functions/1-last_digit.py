#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
print(f"Last digit of {number} is {x} and is", end=" ")
if x > 5:
    print("greater than 5")
elif x == 0:
    print("0")
elif x < 6:
    print("less than 6 and not 0")
