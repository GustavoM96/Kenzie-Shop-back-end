from app.config.database import db

from datetime import datetime
from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, TIMESTAMP


@dataclass
class ShipmentModel(db.Model):
    id: int
    code_post_offices: str
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
