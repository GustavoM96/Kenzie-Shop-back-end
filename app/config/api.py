from flask_restful import Api
from app.views import CustomerResource, CustomerIdResource
from app.views import ProductResource, ProductIdResource
from flask import Flask


def init_app(app: Flask) -> None:
    api = Api(app)

    api.add_resource(CustomerResource, "/customer", endpoint="customer")
    api.add_resource(
        CustomerIdResource, "/customer/<int:customer_id>", endpoint="customer_id"
    )
    api.add_resource(ProductResource, '/product', endpoint="product")
    api.add_resource(ProductIdResource, '/product/<int:product_id>', endpoint="product_id")
