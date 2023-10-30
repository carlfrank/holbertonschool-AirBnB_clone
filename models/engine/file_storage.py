#!/usr/bin/python3
"""FileStorage Module"""

import json


class FileStorage:
    """FileStorage class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            dict_obj = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
            json.dump(dict_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {key: self.__models()
                                        [value["__class__"]](**value)
                                        for key, value in json.load(f).items()}
        except FileNotFoundError:
            pass
