#!/usr/bin/python3
""" Class Place that inherits from BaseModel
takes Place information """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place inherits from BaseModel """
    """ Will be City.id """
    city_id = ""
    """ Will be User.id """
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    """ Will be list of Amenity.id """
    amenity_ids = ()
