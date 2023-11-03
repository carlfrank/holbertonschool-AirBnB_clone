#!/usr/bin/python3
"""Unittest Base Model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test the initialization of the BaseModel class."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
    
    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
