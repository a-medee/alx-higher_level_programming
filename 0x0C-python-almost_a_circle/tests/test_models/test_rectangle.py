#!/usr/bin/python3

""" This module is to test the rectangle module

    File: rectangle.py
    Function: No function
    Class: Base
    Path: ../../models/rectangle.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Hook method for setting up the test fixture
        before exercising it

        Args:
            None

        Returns:
            None
        """
        cls.rec = Rectangle(10, 20)
        cls.rec_1 = Rectangle(2, 10)
        cls.rec_2 = Rectangle(1, 2, 3, 4)

    def test_rectangle_is_intance_of_base(self):
        """Test that a rectangle is an instance of the base class.

        Returns:
            None.
        """
        self.assertIsInstance(self.rec, Base)
        self.assertIsInstance(self.rec_1, Base)

    def test_rectangle_subclass_the_base_class(self):
        """Test that Rectangle inherits from the Base class

        Returns:
            None.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_correct_value_when_initializing_height_or_width_only(self):
        """Test that the correct value is set when initializing a
        rectangle with only height or width.

        Returns:
           None.
        """
        self.assertEqual(self.rec.id, 1)
        self.assertEqual(self.rec.width, 10)
        self.assertEqual(self.rec.height, 20)
        self.assertEqual(self.rec.x, 0)
        self.assertEqual(self.rec.y, 0)

        self.assertEqual(self.rec_1.id, 2)
        self.assertEqual(self.rec_1.width, 2)
        self.assertEqual(self.rec_1.height, 10)
        self.assertEqual(self.rec_1.x, 0)
        self.assertEqual(self.rec_1.y, 0)

    def test_correct_value_when_instance_is_fully_initialized(self):
        """Test that the correct value is set when an instance is fully
        initialized

        Returns:
           None.
        """
        self.assertEqual(self.rec_2.id, 3)
        self.assertEqual(self.rec_2.width, 1)
        self.assertEqual(self.rec_2.height, 2)
        self.assertEqual(self.rec_2.x, 3)
        self.assertEqual(self.rec_2.y, 4)

    def test_error_when_accessing_privates_base_variables_from_within_rectangle(self):
        """This function tests for right errors raised when trying to access
        privates variable of the Base class via either Rectangle or its
        instances

        Args:
            None

        Returns:
            None
        """
        with self.assertRaises(AttributeError):
            print(Rectangle.__nb_objects)

        with self.assertRaises(AttributeError):
            print(self.rec.__nb_objects)
            print(self.rec_1.__nb_objects)

    def test_error_when_accessing_private_variables_from_within_rectangle(self):
        """This function tests for right errors raised when trying to access
        privates variable of the Rectangle class via either Rectangle or its
        instances

        Args:
            None

        Returns:
            None
        """
        with self.assertRaises(AttributeError):
            print(self.rec.__x)
            print(self.rec.__y)
            print(self.rec.__width)
            print(self.rec.__height)

        with self.assertRaises(AttributeError):
            print(Rectangle.__x)
            print(Rectangle.__y)
            print(Rectangle.__width)
            print(Rectangle.__height)

    def test_error_when_accessing_privates_variables_from_within_rectangle(self):
        """This function tests for right errors raised when trying to initialize
        Rectangle with wrong arguments

        Args:
            None

        Returns:
            None
        """
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(12.3, 1, 3)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(12, 1.1, 3)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(12, 1, -3, 1, 4)

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(12, 1, 3, -1, 4)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-12, 1, 3, -1, 4)

    def test_width(self):
        """Test that the width property can be set and retrieved.

        Args:
            self: The unittest instance.

        Returns:
           None.
        """
        self.rec.width = 50
        self.assertEqual(self.rec.width, 50)

    def test_height(self):
        """Test that the height property can be set and retrieved.

        Args:
            self: The unittest instance.

        Returns:
            None.
        """
        self.rec.height = 50
        self.assertEqual(self.rec.height, 50)

    def test_x(self):
        """Test that the x property can be set and retrieved.

        Args:
            self: The unittest instance.

        Returns:
            None.
        """
        self.rec.x = 50
        self.assertEqual(self.rec.x, 50)

    def test_y(self):
        """Test that the y property can be set and
        retrieved.

        Returns:
           None.
        """
        self.rec.y = 50
        self.assertEqual(self.rec.y, 50)


if __name__ == "__main__":
    unittest.main()
