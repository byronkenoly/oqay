#!/usr/bin/env python3.10
"""
User module:
class User that inherits from BaseModel
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    class User

    Attributes:
        email (str): email
        password (str): password
        first_name (str): first name
        last_name (str): last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''    