from sqlalchemy import Column, String, Integer, Float, Text, TIMESTAMP
from app.config.database import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProductModel(db.Model):
    id: int
    name: str
    description: str
    current_price: float
    discount: int
    amount_products: int
    created_at: datetime
    updated_at: datetime
    image_url: str

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String(126), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    current_price = Column(Float, nullable=False)
    discount = Column(Integer, default=0)
    amount_products = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())
    image_url = Column(Text)
