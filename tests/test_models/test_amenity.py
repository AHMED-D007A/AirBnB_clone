#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.model = Amenity()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
