#!/usr/bin/python3
"""This is the File Storage module."""
import json
from datetime import datetime
from os.path import isfile
from models import *


class FileStorage():
    """A serlization and deserlization json files class."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = str(FileStorage.__objects[k])
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as my_file:
            json.dump(store, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as file:
                my_dict = dict(json.load(file))
            for item in my_dict.keys():
                new_dv = FileStorage.__chekker(my_dict[item]["__class__"])
                my_dict.update({item: new_dv})

    def __chekker(self, Class):
        """check if the given object is of the known classes, and return it"""
        from models.base_model import BaseModel
        clss_chekker = {
                        "BaseModel": BaseModel}
        if Class not in clss_chekker.keys():
            return None
        else:
            return clss_chekker[Class]
