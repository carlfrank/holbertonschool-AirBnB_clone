#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_state = State()
        self.my_state.name = "California"

    def test_attributes(self):
        """Test the attributes of State"""
        self.assertEqual(self.my_state.name, "California")


if __name__ == '__main__':
    unittest.main()
