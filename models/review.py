#!/usr/bin/env python3.10
"""
reviews or ratings of products 
submitted by users
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attributes:
        user_id (str): user id
        text (str): actual review
    """
    user_id = ''
    text = ''