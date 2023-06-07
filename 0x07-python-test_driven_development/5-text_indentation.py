#!/usr/bin/python3
"""This module design a function that takes in a string for its
   parameter
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines after
       each of these characters ., ? and :

    Args:
        text(str): the string to parse

    Returns:
        None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    sep_list = [".", "?", ":"]
    is_space = True
    for i in range(0, len(text)):
        if text[i] in sep_list:
            print(text[i], end="\n")
            is_space = True
            print()
            continue
        if text[i - 1] in sep_list and text[i].isspace() or \
           (text[i].isspace() and is_space):
            pass
        else:
            is_space = False
            print(text[i], end="")
