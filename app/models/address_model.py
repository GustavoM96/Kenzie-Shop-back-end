from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, Date


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
    name = Column(String(126), nullable=True)
    number = Column(Integer)
    complement = Column(String(50))
    zipcode = Column(String(9), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now())
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

    customers = relationship("CustomerModel", backref=backref("address"))
