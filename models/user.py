#!/usr/bin/python3
""""this is the User module.."""
from models.base_model import BaseModel


class User(BaseModel):
    """a User class inherites from the BaseModel."""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
