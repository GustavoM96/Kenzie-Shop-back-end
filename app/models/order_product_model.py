from app.config.database import db

from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer,Float


@dataclass
class OrderProductModel(db.Model):
    id: int
    sold_price: float
    quantity_product: int
    total_price: float

    __tablename__ = "orders_products"

    id = Column(Integer, primary_key=True)
    sold_price = Column(Float, nullable=False)
    quantity_product = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    orders = relationship("OrderModel", backref=backref("orders_products"))
    products = relationship("ProductModel", backref=backref("orders_products"))
