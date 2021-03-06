from app.config.database import db
from sqlalchemy import Column, Integer, Boolean, Float

from dataclasses import dataclass


@dataclass
class CartModel(db.Model):
    id: int
    is_empty: bool
    total_price: float

    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)

    is_empty = Column(Boolean, nullable=False, default=True)
    total_price = Column(Float, nullable=False)
