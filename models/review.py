#!/usr/bin/python3
"""
Module to hold class Review
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    class representing a review
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
