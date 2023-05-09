#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if 97 <= ord(i) and ord(i) <= 122:
            result += "{:c}".format((ord(i) - 32))
        else:
            result += "{:c}".format(ord(i))
    print(result)
