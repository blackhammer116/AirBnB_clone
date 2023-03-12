#!/usr/bin/python3
"""
Module to test file_storage.py
"""


from models import storage
from models.base_model import BaseModel
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """
    Tests for class FileStorage
    """

    def test_all_new(self):
        """
        Tests retrieving and creating object from file storage
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        new_dict = {f'{obj1.__class__.__name__}.{obj1.id}': obj1,
                    f'{obj2.__class__.__name__}.{obj2.id}': obj2}
        store_dict = storage.all()
        for key, value in new_dict.items():
            with self.subTest(key=key):
                self.assertIs(store_dict[key], new_dict[key])

        obj3 = BaseModel()
        new_dict[f'{obj3.__class__.__name__}.{obj3.id}'] = obj3
        store_dict = storage.all()

        for key, value in new_dict.items():
            with self.subTest(key=key):
                self.assertIs(store_dict[key], new_dict[key])

    def test_save_reload(self):
        """
        Test the save and reload functionality of file storage
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.save()

        with open("file.json", "r", encoding="utf-8") as f:
            store_dict = json.load(f)

        copy_dict = storage.all().copy()

        for key, value in copy_dict.items():
            copy_dict[key] = value.to_dict()

        self.assertEqual(store_dict, copy_dict)

        copy_dict = storage.all().copy()
        storage.all().clear()

        self.assertEqual(storage.all(), {})
        storage.reload()
        store_dict = storage.all()

        for key, value in store_dict.items():
            with self.subTest(key=key):
                self.assertEqual(store_dict[key].id, copy_dict[key].id)
                self.assertEqual(store_dict[key].created_at,
                                 copy_dict[key].created_at)
                self.assertEqual(store_dict[key].updated_at,
                                 copy_dict[key].updated_at)

        for key, value in copy_dict.items():
            with self.subTest(key=key):
                self.assertEqual(store_dict[key].id, copy_dict[key].id)
                self.assertEqual(store_dict[key].created_at,
                                 copy_dict[key].created_at)
                self.assertEqual(store_dict[key].updated_at,
                                 copy_dict[key].updated_at)
