#!usr/bin/python3
# This class BaseModel
# Defines all common attributes and methods of other classes

from uuid import uuid4
from datetime import date, datetime


class BaseModel:
    # Creating class BaseModel
    id = str(uuid.uuid4())
    
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        _dict = self.__dict__
        _dict['__class__ '] = self.__name__
        _dict['created_at'] = _dict['created_at'].isoformat('%Y-%m-%dT%H:%M:%S.%f')
        _dict['updated_at'] = _dict['updated_at'].isoformat('%Y-%m-%dT%H:%M:%S.%f')
        return _dict

    def __init__(self, *args, **kwags):
        if kwags:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwags["created_at", "%Y-%m-%dT%H:%M:%S.%f"])
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwags["updated_at", "%Y-%m-%dT%H:%M:%S.%f"])
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
