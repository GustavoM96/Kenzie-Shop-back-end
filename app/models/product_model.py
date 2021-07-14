from sqlalchemy import Column, String, Integer, Float, Date, Text, TIMESTAMP
from app.config.database import db
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.schema import ForeignKey


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

    name = Column(String(126), nullable=True, unique=True)
    description = Column(Text, nullable=True)
    current_price = Column(Float, nullable=True)
    discount = Column(Integer, default=0)
    amount_products = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    image_url = Column(Text)
