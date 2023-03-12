#!/usr/bin/python3
"""
   Test module for the class base_model.py
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import time


class TestBaseModel(unittest.TestCase):
    """
    Class to test our BaseModel class
    """

    def test_uuid(self):
        """
        Test that uuid's for our class are unique
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertIsInstance(obj1.id, str)
        self.assertRegex(obj1.id,
                         r"^[0-9ea-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")
        self.assertNotEqual(obj1.id, obj2.id)

    def test_time(self):
        """
        Test the datetime object of BaseModel for time
        """
        obj1 = BaseModel()
        self.assertIsInstance(obj1.created_at, datetime)
        self.assertIsInstance(obj1.updated_at, datetime)
        current_time = datetime.now()
        self.assertLess(obj1.created_at, current_time)
        self.assertLess(obj1.updated_at, current_time)

    def test_str(self):
        """
        test the __str__ magic method of our class
        """
        obj1 = BaseModel()
        output = str(obj1)
        self.assertTrue(output.startswith("[" + obj1.__class__.__name__ + "]"))
        self.assertTrue(output.endswith(str(obj1.__dict__)))
        self.assertRegex(output[output.find("("):output.find(")") + 1],
                         r"^\([0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}\)$")

    def test_save(self):
        """
        Test the save method of the Basemodel class
        """

        obj1 = BaseModel()
        time.sleep(2)
        obj1.save()
        self.assertLess(obj1.created_at, obj1.updated_at)

    def test_dict(self):
        """
        Test the to_dict method of BaseModel
        """

        obj1 = BaseModel()
        temp_dict = obj1.__dict__.copy()
        temp_dict['created_at'] = temp_dict['created_at'].isoformat()
        temp_dict['updated_at'] = temp_dict['updated_at'].isoformat()
        temp_dict['__class__'] = obj1.__class__.__name__
        self.assertEqual(temp_dict, obj1.to_dict())

    def test_kwargs(self):
        """
        Test the initialization of BaseModel via dictionary
        """

        obj1 = BaseModel()
        obj2 = BaseModel(**obj1.to_dict())
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)

        self.assertEqual(obj1.id, obj2.id)
        self.assertEqual(obj1.created_at, obj2.created_at)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

        with self.assertRaises(KeyError):
            obj2.__dict__['__class__']
