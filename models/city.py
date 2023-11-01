#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting BaseModel"""
    state_id = ""
    name = ""
