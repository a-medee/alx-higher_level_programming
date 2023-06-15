#!/usr/bin/python3

"""A script that adds all arguments to a Python list,
and then save them to a file  """

from re import match
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
my_args = str()
my_list = []

with open(filename, "a+", encoding="utf-8") as a_file:
    a_file.seek(0)
    my_args = a_file.read()

    if len(my_args) == 0:
        pass
    else:
        my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
