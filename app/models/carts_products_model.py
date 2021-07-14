from re import U
from app.config.database import db
from sqlalchemy import Column, Integer, DECIMAL
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, backref

from dataclasses import dataclass


@dataclass
class CartProductModel(db.Model):
    id: int
    quantity_id: int
    total_price: int
    cart_id: int
    product_id: int

    __tablename__ = "carts_products"

    id = Column(Integer, primary_key=True)

    quantity_id = Column(Integer, nullable=False)
    total_price = Column(DECIMAL, nullable=False)

    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # TABELAS PIVOS NÃO PODEM TER RELACIONAMENTOS
    # Esses relacionamentos conflitam com os relacionamentos do cart

    # cart = relationship("CartModel", backref=backref("carts_products"))
    # product = relationship(
    #     "ProductModel", backref=backref("carts_products"), uselist=False
    # )
