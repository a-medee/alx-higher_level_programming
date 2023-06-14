#!/usr/bin/python3

""" This modules devises a function named append_after """


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename: a path to the file name
        search_string: the string to be searched
        new_string: the string to insert after search_string

    Returns:
        None
    """

    my_file_list = list()

    with open(filename, "r+", encoding="utf-8") as a_file:
        for line in a_file:
            my_file_list.append(line)

    for line_number in range(len(my_file_list)):
        if search_string in my_file_list[line_number]:
            my_file_list.insert(line_number + 1, new_string)
            line_number += 1

    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write("".join(my_file_list))
