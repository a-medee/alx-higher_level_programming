#!/usr/bin/python3
def print_last_digit(number):
    if (number <= 0):
        lastdigit = -number % 10
        print(f"{lastdigit:d}",end="")
    else:
        lastdigit = number % 10
        print(f"{lastdigit}",end="")
    return (lastdigit)
