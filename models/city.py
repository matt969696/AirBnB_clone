#!/usr/bin/python
""" Definition of Class : City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class attributes and initialization"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of City"""
        super().__init__(*args, **kwargs)
