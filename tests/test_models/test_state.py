#!/usr/bin/python3
"""
Module to test state.py
"""
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Class to test State class
    """

    def test_create(self):
        """
        Test the creation of State object
        """
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertRegex(obj.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")

        self.assertEqual(obj.name, "")

        obj2 = State(**obj.to_dict())
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)
        self.assertEqual(obj.to_dict()['__class__'], State.__name__)
