#!/usr/bin/python
""" Definition of Class : Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class attributes and initialization"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialization of Review"""
        super().__init__(*args, **kwargs)
