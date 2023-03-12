#!/usr/bin/python3

"""define the class BaseModel
"""

from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """defines all attributes/methods common for other classes
    """

    def __init__(self, *args, **kwargs):
        """Public instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    kwargs[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """A public instance method

        Returns:
            str: string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current date/time
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """A public instance method

        Returns:
            _dict_: a dictionary containing key/value pairs of
            __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
