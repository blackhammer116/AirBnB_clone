#!/usr/bin/python3
"""
Module to hold class City
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    class representing a city
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
