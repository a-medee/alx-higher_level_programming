#!/usr/bin/python3

""" This module is to test the base module

    File: base.py
    Function: No function
    Class: Base
    Path: ../../models/base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class created to test the class Base from above

    Attributes:
        None
    """

    def setUp(self) -> None:
        """Hook method for setting up the test fixture
        before exercising it

        Args:
            None

        Returns:
            None
        """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(None)
        self.b4 = Base(12)
        self.b5 = Base(-1)
        self.b6 = Base()
        return super().setUp()

    def tearDown(self):
        """Hook method for deconstructing the test fixture
        after executing it

        Args:
            None

        Returns:
            None
        """
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6
        Base._Base__nb_objects = 0

    def test_got_normal_values_when_id_is_none(self):
        """This function tests for normal values when id is None

        Args:
            None
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b6.id, 4)

    def test_got_normal_values_when_id_is_not_none(self):
        """This function tests for normal values when id is specified
         by the use

         Args:
             None

        Returns:
             None
        """
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, -1)

    def test_error_when_accessing_privates_variables(self):
        """This function tests for right errors raised when trying to access
        privates variable of the Base class via either the class or its
        instances

        Args:
            None

        Returns:
            None
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

        with self.assertRaises(AttributeError):
            print(self.b1.__nb_objects)
            print(self.b2.__nb_objects)
            print(self.b3.__nb_objects)
            print(self.b4.__nb_objects)
            print(self.b5.__nb_objects)
            print(self.b6.__nb_objects)


if __name__ == "__main__":
    unittest.main()
