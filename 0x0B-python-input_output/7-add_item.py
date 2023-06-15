#!/usr/bin/python3

"""A script that adds all arguments to a Python list,
and then save them to a file  """

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
my_args = []

for i in sys.argv[1:]:
    if len(i) != 0:
        my_args.append(i)

save_to_json_file(my_args, filename)

if __name__ == "__main__":
    load_from_json_file(filename)
