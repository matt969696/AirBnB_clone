#!/usr/bin/python
""" Definition of Class : State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class attributes and initialization"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of State"""
        super().__init__(*args, **kwargs)
