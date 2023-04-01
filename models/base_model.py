#!/usr/bin/python3
"""
Base Model module:
defines all common attributes/methods for other classes
"""

import datetime
import models
import  uuid


class BaseModel:
    """
    Public instance attributes.

    Attributes:
        id (str): assign with an uuid when instance is created
                  goal is to have unique id for each BaseModel
        created_at (datetime): assign with current datetime when instance is created.
        updated_at (datetime): assign with current datetime when instance is created and
                               its updated every time you change your object.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        class_name: class name of object
        object_id: get object id
        object_dict: get object dictionary
        """
        class_name = type(self).__name__
        object_id = self.id
        object_dict = self.__dict__
        return f"[{class_name}] ({object_id}) {object_dict}"

    def save(self):
        """
        updates 'updated_at' attribute with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
