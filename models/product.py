#!/usr/bin/env python3.10
"""
Product module:
contains all info related to the product
"""

from .base_model import BaseModel


class Product(BaseModel):
    """
    Product Class

    Attributes:
        name (str): product name
        descriptio (str): product description
        price (int): product price
        stock (int): no. of items remaining
    """
    name = ''
    descriptio = ''
    price = 0
    stock = 0