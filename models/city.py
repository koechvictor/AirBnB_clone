#!/usr/bin/python3
""" Class City that inherits from BaseModel
takes City information """

from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits from BaseModel """
    """ Will be State.id """
    state_id = ""
    name = ""
