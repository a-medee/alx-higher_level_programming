#!/usr/bin/python3
"""This modules devises a class named MyList that inherits from
list
"""


class MyList(list):
    """A class that inherits from a the list type

    Args:
        None

    Attributes:
        None
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """A function that print the list but sorted in ascending
        order

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
