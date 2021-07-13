from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask) -> None:
    app.db = db
    db.init_app(app)

    from app.models.cart_model import CartModel
    from app.models.adress_model import AddressModel
    from app.models.admin_model import AdminModel
    from app.models.products_model import ProductModel
    from app.models.customer_model import CustomerModel
    from app.models.carts_products_model import CartProductModel
