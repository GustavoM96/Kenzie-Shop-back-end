from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP


@dataclass
class OrderProductModel(db.Model):
    id: int
    sold_price: int
    product_quantity: int
    total_price: str

    __tablename__ = 'orders_products'

    
