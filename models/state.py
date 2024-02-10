#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """This is a subclass of BaseModel that represents a state.

    Public class attribute:
        name (str): The name of the state.
    """
    name = ""
