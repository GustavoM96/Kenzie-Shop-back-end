from app.config.database import db
from sqlalchemy import Column, Integer, Float
from sqlalchemy.schema import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.models.product_model import ProductModel


@dataclass
class CartProductModel(db.Model):
    id: int
    quantity_product: int
    total_price: float
    cart_id: int
    product_id: int
    product: ProductModel

    __tablename__ = "carts_products"

    id = Column(Integer, primary_key=True)

    quantity_product = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    product = relationship("ProductModel", backref=backref("cart_products"))
