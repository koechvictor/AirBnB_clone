#!/usr/bin/python3
""" Class BaseModel defines common attributes/methods for other classes"""i

import uuid
from datetime import datetime as dt

class BaseModel:
    ""' Class BaseModel""'

    def __init__(self, *ags, **kwargs):
        """initalize a new instance of BaseModel class
        using argments and keyword arguments """
        
        if kwargs and kwargs != []:
            value = kwargs["created_at"]
            self.id = kwargs["id"]
            self.updated_at = self.created_at
        else:
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def save(self):
        """ updates public instance attribute update_at with current datetime """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """ Returns dictionary containing all the keys/values """

        __dict__ = dict(self.__dict__)
        __dict__['created_at'] = self.created_at.isoformat()
        __dict__['updated_at'] = self.updated_at.isoformat()
        return __dict__
