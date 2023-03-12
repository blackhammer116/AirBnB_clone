#!/usr/bin/python3
"""
Module to test amenity.py
"""
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Class to test Amenity class
    """

    def test_create(self):
        """
        Test the creation of Amenity
        """
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertRegex(obj.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")
        self.assertEqual(obj.name, "")

        obj2 = Amenity(**obj.to_dict())
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)
        self.assertEqual(obj.to_dict()['__class__'], Amenity.__name__)
