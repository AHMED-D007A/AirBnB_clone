#!/usr/bin/python3
"""This is the base module of our classes."""
import uuid
from datetime import datetime
import sys
import models


class BaseModel():
    """This is the BaseModel class the base of site's classes."""

    def __init__(self, *args, **kwargs):
        """the initialization method for all out attributes."""
        if kwargs:
            for k in kwargs:
                if k == "__class__":
                    setattr(self, k, getattr(sys.modules[__name__], kwargs[k]))
                    continue
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                    continue
                setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """print the informal string representation."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dicc = self.__dict__.copy()
        dicc["__class__"] = "BaseModel"
        dicc["created_at"] = str(dicc["created_at"].isoformat())
        if ("updated_at" in dicc):
            dicc["updated_at"] = str(dicc["updated_at"].isoformat())
        return dicc
