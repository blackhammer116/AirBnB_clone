#!/usr/bin/python3
"""
Module to test review.py
"""
from models.review import Review
import unittest
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Class to test Review class
    """

    def test_create(self):
        """
        Test the creation of Review
        """
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertRegex(obj.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")

        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")

        obj2 = Review(**obj.to_dict())
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)
        self.assertEqual(obj.to_dict()['__class__'], Review.__name__)
