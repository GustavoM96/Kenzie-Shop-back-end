from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP


@dataclass
class AddressModel(db.Model):
    id: int
    name: str
    number: int
    complement: str
    zipcode: str
    city: str
    state: str
    created_at: datetime
    updated_at: datetime

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    name = Column(String(126), nullable=False)
    number = Column(Integer)
    complement = Column(String(50))
    zipcode = Column(String(9), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customers = relationship("CustomerModel", backref=backref("address"))
