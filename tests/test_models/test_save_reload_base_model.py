#!/usr/bin/python3
"""Unittest Base File Storage"""

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test methods."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        # Make sure to start with a clean slate for each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up tasks."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that 'all' returns the dictionary of objects."""
        returned_objects = self.storage.all()
        self.assertIsInstance(returned_objects, dict)

    def test_new(self):
        """Test that 'new' correctly adds objects."""
        test_model = BaseModel()
        self.storage.new(test_model)
        key = f"{type(test_model).__name__}.{test_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that 'save' correctly serializes objects to file."""
        test_model = BaseModel()
        self.storage.new(test_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            objects = json.load(f)
            key = f"{type(test_model).__name__}.{test_model.id}"
            self.assertIn(key, objects)

    def test_reload(self):
        """Test that 'reload' correctly deserializes objects from file."""
        test_model = BaseModel()
        self.storage.new(test_model)
        self.storage.save()
        self.storage.reload()
        key = f"{type(test_model).__name__}.{test_model.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
