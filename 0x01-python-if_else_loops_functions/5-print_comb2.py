#!/usr/bin/python3
i = 0
while (i < 100):
    if i != 99:
        print(f"{i:02d}", end=", ")
        i += 1
        continue
    print(f"{i:d}")
    i += 1
