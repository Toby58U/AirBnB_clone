#!/usr/bin/python3
"""Defines an abstracted FileStorage class."""
import json
from os.path import isfile
from base_model import BaseModel

class FileStorage:
    """This represents an abstracted storage engine.

    Class attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.

    Class methods:
        all: returns the dictionary  _objects.
        new: sets new __objects to existing dictionary of instances.
        save: Serializes.
        reload: Deserializes.
    """
    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        objname = obj.__class__.__name__
        k = f"{objname}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for k, obj in self.__objects.items():
            serialized_objects[k] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects.
        Only reloads if the JSON file (__file_path) exists.
        If the file doesn’t exist, no exception should be raised.
        """
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for k, obj_dict in data.items():
                    class_name, obj_id = k.split('.')
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[k] = obj
