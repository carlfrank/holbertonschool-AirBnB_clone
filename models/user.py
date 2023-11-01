#!/usr/bin/python3
"""User module"""

from base_model import BaseModel


class User(BaseModel):
    """User class inheriting BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
