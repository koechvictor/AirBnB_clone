#!/usr/bin/python3
""" Class Review that inherits from BaseModel
takes Review information """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review inherits from BaseModel """
    """ Will be Place.id """
    place_id = ""
    """ Will be User.id """
    user_id = ""
    text = ""
