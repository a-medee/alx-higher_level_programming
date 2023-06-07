#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ This class is used as a unitest class for the
    max_integer function
    """
    def setUp(self) -> None:
        """Hook method for setting up the test fixture before
        exercising it
        """
        self.my_list = [1, 3, 4, 5, 6]
        self.my_list_1 = [-1, -2, 4, 5, 6]
        self.my_list_2 = [-1, -2, -4, -5, -12346]
        self.my_list_3 = []
        self.my_list_4 = [1]
        self.my_list_6 = ["", 3, 5, 7, "9"]
        self.my_list_7 = [1, 3, 3, -1, -1, -1]
        self.my_list_8 = [1, 1, 1, 1, 1]
        self.my_list_9 = [1, 3, 4, -1, None]
        self.my_list_10 = [None, None, None, None]
        self.my_list_11 = [None, None, None, None, 1, -1002]
        self.my_list_12 = [None, None, None, None, 1 , " ", "This is None"]
        return super().setUp()

    def tearDown(self) -> None:
        """Hook metod for deconstructing the test fixture after
        testing it
        """
        return super().tearDown()

    def test_good_return(self):
        """A test function that ensures the good
        values is return in normal cases
        """
        self.assertEqual(max_integer(self.my_list), 6)
        self.assertEqual(max_integer(self.my_list_1), 6)
        self.assertEqual(max_integer(self.my_list_2), -1)

    def test_empty_case(self):
        """Test the function return in empty case
        """
        self.assertEqual(max_integer(self.my_list_3), None)

    def test_one_value(self):
        """Test the function return in case it's passed 1 int object
        """
        self.assertEqual(max_integer(self.my_list_4), 1)

    def test_unwanted_value(self):
        """Test the function return when it's passed non-integer values
        """
        self.assertRaises(TypeError, max_integer, self.my_list_6)
        self.assertRaises(TypeError, max_integer, self.my_list_9)
        self.assertRaises(TypeError, max_integer, self.my_list_10)
        self.assertRaises(TypeError, max_integer, self.my_list_11)
        self.assertRaises(TypeError, max_integer, self.my_list_12)

    def test_same_value(self):
        """Test the function return when it's passed list_with the same value
        in a certain range
        """
        self.assertEqual(max_integer(self.my_list_7), 3)
        self.assertEqual(max_integer(self.my_list_8), 1)


if __name__ == "__main__":
    unittest.main()
