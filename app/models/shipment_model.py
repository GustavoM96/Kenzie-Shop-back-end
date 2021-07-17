from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean


@dataclass
class ShipmentModel(db.Model):
    id: int
    postal_code: str
    was_dispatch: bool
    status: str
    arrival_date: datetime
    post_date: datetime
    name: str
    number: int
    complement: str
    zipcode: str
    city: str
    state: str

    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    postal_code = Column(String(20))
    was_dispatch = Column(Boolean)
    status = Column(String)
    arrival_date = Column(TIMESTAMP)
    post_date = Column(TIMESTAMP)
    name = Column(String(50), nullable=False)
    number = Column(Integer)
    complement = Column(String(50))
    zipcode = Column(String(9), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"))

    order = relationship("OrderModel", backref=backref("shipments"))
