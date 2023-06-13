#!/usr/bin/python3
""" This module devises a named read_file """


def read_file(filename=""):
    """A funtion that reads a text file and prints it
    to stdout

    Args:
        filename: a file name

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end="")
