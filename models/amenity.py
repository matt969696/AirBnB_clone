#!/usr/bin/python
""" Definition of Class : Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class attributes and initialization"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of Amenity"""
        super().__init__(*args, **kwargs)
