#!/usr/bin/python3
"""
Module to hold class State
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    class representing a state
    """

    name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
