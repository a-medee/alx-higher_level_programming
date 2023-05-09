#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) and ord(i) <= 122:
            print(f"{(ord(i) - 32):c}", end="")
        else:
            print(f"{(ord(i)):c}", end="")
