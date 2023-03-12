#!/usr/bin/python3
"""
Module to hold FileStorage class
"""
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
import json


class FileStorage:
    """
    Abstraction for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all object instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object tot he object instances dictionary
        """
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes all object instances to file
        """
        copy_dict = FileStorage.__objects.copy()
        for key, value in copy_dict.items():
            copy_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(copy_dict, f)

    def reload(self):
        """
        Deserializes file data to object instances
        """
        read_dict = None
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                read_dict = json.load(f)
        except FileNotFoundError:
            pass
        if read_dict:
            new_dict = {}
            for key, value in read_dict.items():
                if value['__class__'] == BaseModel.__name__:
                    new_dict[key] = BaseModel(**value)
                elif value['__class__'] == User.__name__:
                    new_dict[key] = User(**value)
                elif value['__class__'] == Amenity.__name__:
                    new_dict[key] = Amenity(**value)
                elif value['__class__'] == City.__name__:
                    new_dict[key] = City(**value)
                elif value['__class__'] == Place.__name__:
                    new_dict[key] = Place(**value)
                elif value['__class__'] == Review.__name__:
                    new_dict[key] = Review(**value)
                elif value['__class__'] == State.__name__:
                    new_dict[key] = State(**value)
                else:
                    raise TypeError("Unknown Class")
            FileStorage.__objects = new_dict
