#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arguments_list = sys.argv
    size_argument_list = len(sys.argv) - 1
    sum = 0

    if size_argument_list == 0:
        print("{:d}".format(sum))
    elif size_argument_list == 1:
        sum += int(arguments_list[1])
        print("{:d}".format(sum))
    elif size_argument_list > 1:
        for i in range(1, size_argument_list + 1):
            sum += int(arguments_list[i])

        print("{:d}".format(sum))
