from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP


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
    
