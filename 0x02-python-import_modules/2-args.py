#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arguments_list = sys.argv
    size_argument_list = len(sys.argv) - 1

    if size_argument_list == 0:
        print("{:d} argument.".format(size_argument_list))
    elif size_argument_list == 1:
        print("{:d} argument:".format(size_argument_list))
        print("{:d}: {:s}".format(1, arguments_list[1]))
    elif size_argument_list > 1:
        print("{:d} arguments:".format(size_argument_list))
        for i in range(1, size_argument_list + 1):
            print("{:d}: {:s}".format(i, arguments_list[i]))
