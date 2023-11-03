import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up"""
        self.city = City()

    def test_name(self):
        """Test name"""
        self.assertEqual(self.city.name, '')

    def test_state_id(self):
        """Test state_id"""
        self.assertEqual(self.city.state_id, '')

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'id'))

    def test_attribute_defaults(self):
        """Test attribute defaults"""
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')

    
if __name__ == '__main__':
    unittest.main()
