#!/usr/bin/python3
i = 0
while (i < 100):
    if i != 99:
        print("{:02d}".format(i), end=", ")
        i += 1
        continue
    print("{:d}".format(i))
    i += 1
