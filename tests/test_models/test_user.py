#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        print("-- Create a new User --")
        self.my_user = User()
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Bar"
        self.my_user.email = "airbnb@mail.com"
        self.my_user.password = "root"
        self.my_user.save()
        print(self.my_user)
        print("-- Create a new User 2 --")
        self.my_user2 = User()
        self.my_user2.first_name = "John"
        self.my_user2.email = "airbnb2@mail.com"
        self.my_user2.password = "root"
        self.my_user2.save()
        print(self.my_user2)

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertEqual(self.my_user.last_name, "Bar")
        self.assertEqual(self.my_user.email, "airbnb@mail.com")
        self.assertEqual(self.my_user.password, "root")
        self.assertEqual(self.my_user2.first_name, "John")
        self.assertEqual(self.my_user2.email, "airbnb2@mail.com")
        self.assertEqual(self.my_user2.password, "root")


if __name__ == '__main__':
    unittest.main()
