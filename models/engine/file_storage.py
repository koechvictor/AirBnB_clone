#!/usr/bin/python3
"""  Class FileStorage the serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
import os

class FileStorage:
    """ Class FileStorage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
            """ serializes __objects to the JSON file _file_path """
            dict_obj = {}
            for key, value in Filestorage.__object.items():
                dict_obj[key] = value.to_dict()
                with open(Filestorage.__file_path, "w") as f:
                    json.dump(dict_obj, f)

      def reload(self):
          """ Deserializes tyhe JSON file to __objects if __file_path exists
          otherwise do nothing with no exeption being raised """
          #if file doesn't exists it returns
          file_name = Filestorage._file_path
          if (not os.path.exists(file_name)) or os.stat(file_name).st_size == 0:
              return
          from models.base_model import BaseModel
          from models.city import City
          from models.user import User
          from models.place import place

          with open(FileStorage.__file_path, "r") as f:
              thing = json.load(f)


