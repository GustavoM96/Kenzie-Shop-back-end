from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP


@dataclass
class ShipmentModel(db.Model):
    id: int
    postal_code: str
    status: str
    arrival_date: datetime
    post_date: datetime
    shipping_price: int
    name: str
    number: int
    complement: str
    zipcode: str
    city: str
    state: str

    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    postal_code = Column(String(20))
    status = Column(String)
    arrival_date = Column(TIMESTAMP)
    post_date = Column(TIMESTAMP)
    shipping_price = Column(Integer)
    name = Column(String(50), nullable=False)
    number = Column(Integer)
    complement = Column(String(50))
    zipcode = Column(String(9), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))

    orders = relationship("OrderModel", backref=backref("shipments"))
