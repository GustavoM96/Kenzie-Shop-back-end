from app.config.database import db
from sqlalchemy import Column, Integer, Float, UniqueConstraint, TIMESTAMP
from sqlalchemy.schema import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.models.product_model import ProductModel
from datetime import datetime


@dataclass
class CartProductModel(db.Model):
    id: int
    quantity_product: int
    total_price: float
    cart_id: int
    product_id: int
    product: ProductModel

    __tablename__ = "carts_products"

    __table_args__ = (
        UniqueConstraint("cart_id", "product_id", name="cart_product_uc"),
    )
    id = Column(Integer, primary_key=True)

    quantity_product = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())

    product = relationship("ProductModel", backref=backref("carts_products"))
    cart = relationship("CartModel", backref=backref("carts_products"))
