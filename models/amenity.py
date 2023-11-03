#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inheriting BaseModel"""
    name = ""

    def __str__(self):
        """Returns a string representation of the Amenity instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
