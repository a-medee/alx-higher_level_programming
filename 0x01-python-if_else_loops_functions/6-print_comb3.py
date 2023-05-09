#!/usr/bin/python3
i = 0
while i < 10:
    j = 0
    while j < 10:
        if j > i and (i != 9 and i != 8):
            print(f"{i:d}{j:d}", end=", ")
        if j == 9 and i == 8:
            print(f"{i:d}{j:d}")
        j += 1
    i += 1
