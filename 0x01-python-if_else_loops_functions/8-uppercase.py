#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) and ord(i) <= 122:
            print("{:c}".format((ord(i) - 32)), end="")
        else:
            print("{:c}".format(ord(i)), end="")
    print("")
