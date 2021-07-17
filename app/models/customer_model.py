from datetime import datetime
from app.config.database import db
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.schema import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from app.exc import PasswordError


@dataclass
class CustomerModel(db.Model):
    id: int
    name: str
    last_name: str
    email: str
    cart_id: int
    create_at: datetime
    update_at: datetime

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    name = Column(String(126), nullable=False)
    last_name = Column(String(126), nullable=False)
    email = Column(String(126), nullable=False, unique=True)
    password_hash = Column(String(126), nullable=False)
    cart_id = Column(Integer, ForeignKey("carts.id"), unique=True, nullable=False)
    create_at = Column(TIMESTAMP, default=datetime.now())
    update_at = Column(TIMESTAMP, default=datetime.now())

    cart = relationship("CartModel", backref=backref("customer"), uselist=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_copare):
        check_password = check_password_hash(self.password_hash, password_to_copare)

        if not check_password:
            raise PasswordError()

        return check_password
