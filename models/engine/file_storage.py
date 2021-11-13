#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile
import models


def reload(self):
    ''' loads data from file '''
    clss = models.models
    if not isfile(self._FileStorage__file_path):
        return
    with open(self._FileStorage__file_path, 'r') as file:
        js_objs = json.load(file)
        self._FileStorage__objects.clear()
        # self.__objects = {}
        for k, v in js_objs.items():
            cls = clss[v['__class__']]
            self._FileStorage__objects[k] = cls(**v)


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}
    reload = reload

    def __init__(self):
        ''' initializes a storage engine '''
        pass

    def all(self):
        ''' gets all objects '''
        return self.__objects

    def new(self, obj):
        ''' registers a new object '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__file_path, 'w') as file:
            r_objs = self.__objects
            objs = {}
            for k in r_objs:
                v = r_objs[k]
                objs[k] = v.to_dict()
            json.dump(objs, file)
