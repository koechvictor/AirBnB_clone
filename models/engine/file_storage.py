#!/usr/bin/python3
""" Class FileStorage the serializes instances to a JSON file
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
        """ Sets in __objects the obj with key <obj class name>.id """

        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file __file_path """
        dict_obj = {}
        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects if __file_path exists
        otherwise do nothing, with no exception being reaised """
        # if file doesnt exists it returns
        file_name = FileStorage.__file_path
        if (not os.path.exists(file_name)) or os.stat(file_name).st_size == 0:
            return
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State,
                   "User": User}
        with open(FileStorage.__file_path, "r") as f:
            thing = json.load(f)
        for key, value in thing.items():
            if value['__class__'] in classes.keys():
                value = classes[key.split(".")[0]](**value)
                FileStorage.__objects.update({key: value})
            else:
                print("** class doesn't exist **")
                FileStorage.__objects.update({key: None})
