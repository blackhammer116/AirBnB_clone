#!/usr/bin/python3
"""
Module to test place.py
"""
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Class to test Place class
    """

    def test_create(self):
        """
        Test the creation of Place
        """
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertRegex(obj.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")

        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertAlmostEqual(obj.latitude, 0.0)
        self.assertAlmostEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

        obj2 = Place(**obj.to_dict())
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)
        self.assertEqual(obj.to_dict()['__class__'], Place.__name__)
