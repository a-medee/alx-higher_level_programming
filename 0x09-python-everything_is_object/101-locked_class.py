#!/usr/bin/python3
"""This moduled devises a way to prevent dynamic allocation
"""


class LockedClass(object):
    """This class is built with the idea to prevent the user
    from dynamicly creating attributes to the class

    Attributes:
        __slots__(list): a builtins attribute that helps
    preventing the user from creating dynamics variables
    """
    __slots__ = ['first_name']
