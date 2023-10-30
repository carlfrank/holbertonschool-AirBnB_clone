#!/usr/bin/python3
"""Base_Models Module"""

import uuid
from datetime import datetime


class BaseModels:
    """BaseModels class"""
    id = uuid.uuid4
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self):
        """initialize variables"""
        id = uuid.uuid4
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """print a string"""
        return f"[{self.__class__.__name__}] (self.id) (self.__dict__)"

    def save(self):
        """Saves info"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a dictionary and turns them into a dictionary"""
        class_dict = dict(self.__dict__)
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
