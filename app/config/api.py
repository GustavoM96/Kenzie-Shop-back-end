from flask_restful import Api
from app.views import CustomerResource
from flask import Flask


def init_app(app: Flask) -> None:
    api = Api(app)
    api.add_resource(CustomerResource, "/customer", endpoint="customer")
