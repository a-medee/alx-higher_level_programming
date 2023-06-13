#!/usr/bin/python3
""" This module devises a function named write_file """


def write_file(filename="", text=""):
    """A funtion a function that writes a string to a text file
    (UTF8) and returns the number of characters written

    Args:
        filename: file name
        text: a text to write into filename(the first param)

    Returns:
        an int object
    """

    nbre_write = int()
    with open(filename, "w", encoding="utf-8") as a_file:
        nbre_write = a_file.write(text)

    return nbre_write
