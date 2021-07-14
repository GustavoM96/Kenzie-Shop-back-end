from flask_restful import Api
from app.views import CustomerResource, CustomerIdResource
from app.views import ProductResource, ProductIdResource
from app.views import AddressIdCustomerResource, AdressIdResource
from app.views import AuthCustomerResource, AuthAdminResource
from app.views import AdminResource
from flask import Flask


def init_app(app: Flask) -> None:
    api = Api(app)

    api.add_resource(CustomerResource, "/customer", endpoint="customer")
    api.add_resource(AdminResource, "/admin", endpoint="admin")

    api.add_resource(
        CustomerIdResource, "/customer/<int:customer_id>", endpoint="customer_id"
    )
    api.add_resource(ProductResource, "/product", endpoint="product")
    api.add_resource(
        ProductIdResource, "/product/<int:product_id>", endpoint="product_id"
    )

    api.add_resource(
        AddressIdCustomerResource,
        "/customer/<int:customer_id>/address",
        endpoint="address",
    )
    api.add_resource(
        AdressIdResource, "/address/<int:address_id>", endpoint="address_id"
    )

    api.add_resource(
        AuthCustomerResource, "/auth/customer", endpoint="authenticate_customer"
    )
    api.add_resource(AuthAdminResource, "/auth/admin", endpoint="authenticate_admin")
