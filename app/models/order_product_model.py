from app.config.database import db

from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer


@dataclass
class OrderProductModel(db.Model):
    id: int
    sold_price: int
    product_quantity: int
    total_price: str

    __tablename__ = "orders_products"

    id = Column(Integer, primary_key=True)
    sold_price = Column(Integer, nullable=False)
    product_quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    orders = relationship("OrderModel", backref=backref("orders_products"))
    products = relationship("ProductModel", backref=backref("orders_products"))
