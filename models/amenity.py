#!/usr/bin/python3
"""this is the Amenity module."""
from base_model import BaseModel


class Amenity(BaseModel):
    """a Amenity class inherites from the BaseModel."""
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
