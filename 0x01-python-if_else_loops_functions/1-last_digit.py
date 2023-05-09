#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number <= 0):
    lastdigit = -number % 10
    lastdigit *= -1
else:
    lastdigit = number % 10

print(f"Last digit of {number:d} is {lastdigit:d}", end=" ")
if lastdigit == 0:
    print("and is 0")
elif lastdigit > 5:
    print("and is greater than 5")
elif (lastdigit < 6 and lastdigit != 0):
    print("and is less than 6 and not 0")
