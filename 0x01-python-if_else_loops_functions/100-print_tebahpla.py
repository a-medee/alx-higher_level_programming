#!/usr/bin/python3
a = 122
while (a >= 97):
    if a % 2 == 0:
        tobe = chr(a)
    else:
        tobe = chr(a - 32)
    print("{}".format(tobe), end="")
    a -= 1
