from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask) -> None:
    app.db = db
    db.init_app(app)

    from app.models.cart_model import CartModel
    from app.models.address_model import AddressModel
    from app.models.admin_model import AdminModel
    from app.models.product_model import ProductModel
    from app.models.customer_model import CustomerModel
    from app.models.carts_products_model import CartProductModel
    from app.models.order_model import OrderModel
    from app.models.order_product_model import OrderProductModel
    # from app.models.shipment_model import ShipmentModel
