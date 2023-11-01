#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
