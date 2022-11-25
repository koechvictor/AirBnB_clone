#!/usr/bin/python3
""" class user that inherits from BaseModel
takes in user infomation """

from models.base_model import BaseModel

class User(BaseModel):
    """ Class User inherits from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
