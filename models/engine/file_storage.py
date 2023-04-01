#!/usr/bin/python3
"""
FileStorage module:
serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json
from os import path


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
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
