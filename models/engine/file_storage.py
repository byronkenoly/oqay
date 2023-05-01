#!/usr/bin/env python3.10
"""
FileStorage module:
serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json
from os import path
from models.base_model import BaseModel
from models.product import Product
from models.review import Review
from models.user import User


class FileStorage:
    """
    Private class attributes.

    Attributes:
        __file_path (str): path to the JSON file that stores contents of `__objects`
        __objects (dict): stores all objects by <class name>.id
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212
        """
        class_name = obj.__class__.__name__
        obj_id = obj.id
        self.__objects[f"{class_name}.{obj_id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file

        json.dump() is used to write the serialized JSON string directly to a file object
        It takes 2 args:
        1. Python object to serialize
        2. File object where the serialized JSON string will be written to
        """
        json_dict = {}
        for key, val in self.__objects.items():
            json_dict[key] = val.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    self.__objects[key] = eval(val['__class__'])(**val)
