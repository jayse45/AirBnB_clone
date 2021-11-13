#!usr/bin/python3

import json
from model.base_model import BaseModel

class FileStorage:
    """
    Private class attributes:
    __file_path
    __objects
    Public instance methods:
    all(self)
    new(self, obj)
    save(self)
    reload(self)
    """
    
    __file._path = str("")
    __objects = dict()
    
    def all(self):
        """  Returns the dictionary __objects """
        return self.__objects
        
    def new(self, obj):
        """  Sets in __objects the obj with key <obj class name>.id """
        if obj:
            res = obj.__class__.__name__ + "." + obj.id
            self.__objects[res] = obj
    
