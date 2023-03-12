#!/usr/bin/python3
"""
Module to hold class Place
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    class representing a place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
