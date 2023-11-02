#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_city = City()
        self.my_city.state_id = "CA"
        self.my_city.name = "San Francisco"

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertEqual(self.my_city.state_id, "CA")
        self.assertEqual(self.my_city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
