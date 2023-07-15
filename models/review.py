#!/usr/bin/python3
"""this is the Review module."""
from base_model import BaseModel


class Review(BaseModel):
    """a Review class inherites from the BaseModel."""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
