from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean


@dataclass
class OrdersModel(db.Model):
    id: int
    customer_id: int
    invoice_url: str
    was_paid: bool
    total_price: int
    shipping_price: int
    total:int 
    created_at: datetime
    payment_type: str

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    invoice_url = Column(String)
    was_paid = Column(Boolean, nullable=False)
    total_price = Column(Integer, nullable=False)
    shipping_price = Column(Integer)
    total = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    payment_type = Column(String(20))

    customers = relationship("CustomerModel", backref=backref("orders"))
    addresses = relationship("AddressModel", backref=backref("orders"))
        
