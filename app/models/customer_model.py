from datetime import datetime
from app.config.database import db
from sqlalchemy import Column, String, Integer, Date
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CustomerModel(db.Model):
    name: str
    last_name: str
    email: str
    cart_id: int
    create_at: datetime
    update_at: datetime

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    name = Column(String(126), nullable=True)
    last_name = Column(String(126), nullable=True)
    email = Column(String(126), nullable=True)
    password_hash = Column(String(126), nullable=True)
    cart_id = Column(Integer)
    create_at = Column(Date, default=datetime.now())
    update_at = Column(Date, default=datetime.now())

    cart = relationship("CartModel", backref=backref("customer"), uselist=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_copare):
        return check_password_hash(self.password_hash, password_to_copare)
