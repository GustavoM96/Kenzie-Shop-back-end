from app.config.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class AdminModel(db.Model):
    id: int
    name: str
    email: str

    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    name = Column(String(126), nullable=True)  # this one is Silvão
    email = Column(String(126), nullable=False, unique=True)
    password_hash = Column(String(522), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not acessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_copare):
        return check_password_hash(self.password_hash, password_to_copare)
