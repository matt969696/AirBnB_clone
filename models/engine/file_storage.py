#!/usr/bin/python3
"""
    Module with definition of class : File Storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classlist = {"BaseModel": BaseModel, "User": User, "State": State,
             "City": City, "Amenity": Amenity, "Place": Place,
             "Review": Review}


class FileStorage():
    """Class FileStroage used by the console with JSON"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        myjson = {}
        for key in self.__objects:
            myjson[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(myjson, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                j = json.load(f)
            for key in j:
                self.__objects[key] = classlist[j[key]["__class__"]](**j[key])
        except:
            pass
