from app.config.database import db
from sqlalchemy import Column, Integer, Boolean, Float
from sqlalchemy.orm import relationship, backref

from dataclasses import dataclass


@dataclass
class CartModel(db.Model):
    id: int
    is_empty: bool
    total_price: float

    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)

    is_empty = Column(Boolean, nullable=False)
    total_price = Column(Float, nullable=False)

    products = relationship(
        "ProductModel", secondary="carts_products", backref=backref("carts")
    )
