#!/usr/bin/python3
def print_last_digit(number):
    if (number <= 0):
        lastdigit = -number % 10
        lastdigit *= -1
    else:
        lastdigit = number % 10

    return (lastdigit)
