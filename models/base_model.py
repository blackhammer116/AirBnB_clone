#!/usr/bin/python3
"""
Module to hold the class BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class that is going to be base for all other Classes in our project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class with uuid and datetime objects
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the class
        """

        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """
        Save the object and update its last updated
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary that represents the object
        """
        dict_ret = self.__dict__.copy()
        dict_ret['created_at'] = dict_ret['created_at'].isoformat()
        dict_ret['updated_at'] = dict_ret['updated_at'].isoformat()
        dict_ret['__class__'] = self.__class__.__name__
        return dict_ret
