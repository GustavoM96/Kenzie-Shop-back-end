from app.config.database import db
from sqlalchemy import Column, Integer, Float
from sqlalchemy.schema import ForeignKey

from dataclasses import dataclass


@dataclass
class CartProductModel(db.Model):
    id: int
    quantity_id: int
    total_price: float
    cart_id: int
    product_id: int

    __tablename__ = "carts_products"

    id = Column(Integer, primary_key=True)

    quantity_id = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
