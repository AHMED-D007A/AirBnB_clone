#!/usr/bin/python3
"""this is the State module."""
from base_model import BaseModel


class State(BaseModel):
    """a State class inherites from the BaseModel."""
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
