from flask_restful import Api
from app.views import CustomerResource, CustomerIdResource
from flask import Flask


def init_app(app: Flask) -> None:
    api = Api(app)

    api.add_resource(CustomerResource, "/customer", endpoint="customer")
    api.add_resource(
        CustomerIdResource, "/customer/<int:customer_id>", endpoint="customer_id"
    )
