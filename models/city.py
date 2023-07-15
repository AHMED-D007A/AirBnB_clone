#!/usr/bin/python3
"""this is the City module."""
from base_model import BaseModel


class City(BaseModel):
    """a City class inherites from the BaseModel."""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
