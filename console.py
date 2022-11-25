#!/usr/bin/python3
""" console for AirBnb """
import cmd
import ast
from datetime import datetime as dt
from models.__init__import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel,
           "Aminity": Amenity,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User}

        def do_create(self,args):
            """ creates a new instance of BaseModel """
            if not args:
                print ("** class name missing **")
            elif args in classes.keys():
                new = classes[args]()
                new.save()
                storage.reload()
                print(new.id)
            else:
                print("** class doesn't exist **")

          def do_show(self, args):
              """ shows instances based on class and id
              args comes in as two values class and id (class ID> """
              if not args:
                  print("** class name missing **")
                  return
              args = args.split()
              objs = storage.all()
              if not args[0] in classes.keys():
                    print("** class doesn't exist **")
              elif len(args) < 2:
                  print("** instance id missing **")
              else:
                  for key in objs.keys():
                       if args[1] in key.split(".")[1]:
                           print(objs[key])
                           return
                       print("** no instance found **")
