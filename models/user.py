#!/usr/bin/python
""" Definition of Class : User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class attributes and initialization"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization of user"""
        super().__init__(*args, **kwargs)
