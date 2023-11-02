#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_place = Place()
        self.my_place.city_id = "SF"
        self.my_place.user_id = "user1"
        self.my_place.name = "My Place"
        self.my_place.description = "A nice place"
        self.my_place.number_rooms = 3
        self.my_place.number_bathrooms = 2
        self.my_place.max_guest = 4
        self.my_place.price_by_night = 100
        self.my_place.latitude = 37.7749
        self.my_place.longitude = -122.4194
        self.my_place.amenity_ids = ["amenity1", "amenity2"]

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertEqual(self.my_place.city_id, "SF")
        self.assertEqual(self.my_place.user_id, "user1")
        self.assertEqual(self.my_place.name, "My Place")
        self.assertEqual(self.my_place.description, "A nice place")
        self.assertEqual(self.my_place.number_rooms, 3)
        self.assertEqual(self.my_place.number_bathrooms, 2)
        self.assertEqual(self.my_place.max_guest, 4)
        self.assertEqual(self.my_place.price_by_night, 100)
        self.assertEqual(self.my_place.latitude, 37.7749)
        self.assertEqual(self.my_place.longitude, -122.4194)
        self.assertEqual(self.my_place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
