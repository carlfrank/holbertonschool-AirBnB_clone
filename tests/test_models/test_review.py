#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_review = Review()
        self.my_review.place_id = "place1"
        self.my_review.user_id = "user1"
        self.my_review.text = "Great place!"

    def test_attributes(self):
        """Test the attributes of Review"""
        self.assertEqual(self.my_review.place_id, "place1")
        self.assertEqual(self.my_review.user_id, "user1")
        self.assertEqual(self.my_review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
