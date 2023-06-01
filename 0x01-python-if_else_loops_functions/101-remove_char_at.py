#!/usr/bin/python3
def remove_char_at(str, n):
    result = ''
    for i, j in enumerate(str):
        if i != n:
            result += str[i]
    return (result)
