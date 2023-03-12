#!/usr/bin/python3
"""
Module to test user.py
"""
from models.user import User
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Class to test User class
    """

    def test_create(self):
        """
        Test the creation of User
        """
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertRegex(obj.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
        obj2 = User(**obj.to_dict())
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)
        self.assertEqual(obj.to_dict()['__class__'], User.__name__)
