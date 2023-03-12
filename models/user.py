#!/usr/bin/python3
"""
Module to hold class User
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    class representing a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
