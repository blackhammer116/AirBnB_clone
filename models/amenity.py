#!/usr/bin/python3
"""
Module to hold class Amenity
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    class representing a amenity
    """

    name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
