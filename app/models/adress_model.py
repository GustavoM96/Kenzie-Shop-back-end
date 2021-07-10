from datetime import datetime
from app.config.database import db
from sqlalchemy import Column, String, Integer, Date


class adressModel(db.Model):
    __tablename__ = "adress"

    id = Column(Integer, primary_key=True)
    name = Column(String(126), nullable=True)
    number = Column(Integer)
    complement = Column(String(50))
    zipcode = Column(String(9), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    create_at = Column(Date, default=datetime.now())
    update_at = Column(Date, default=datetime.now())
