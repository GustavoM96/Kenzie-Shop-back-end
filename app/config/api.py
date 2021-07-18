from flask_restful import Api
from app.views import CustomerResource, CustomerIdResource
from app.views import CartResource, CartProductResource
from app.views import ProductResource, ProductIdResource
from app.views import AddressIdCustomerResource, AdressIdResource
from app.views import AuthCustomerResource, AuthAdminResource
from app.views import AdminResource
from flask import Flask


def init_app(app: Flask) -> None:
    api = Api(app)

    api.add_resource(AdminResource, "/admins", endpoint="admin")
    api.add_resource(CustomerResource, "/customers", endpoint="customer")

    api.add_resource(
        CustomerIdResource, "/customers/<int:customer_id>", endpoint="customer_id"
    )
    api.add_resource(ProductResource, "/products", endpoint="product")
    api.add_resource(
        ProductIdResource, "/products/<int:product_id>", endpoint="product_id"
    )

    api.add_resource(
        AddressIdCustomerResource,
        "/customers/<int:customer_id>/addresses",
        endpoint="address",
    )
    api.add_resource(
        AdressIdResource, "/addresses/<int:address_id>", endpoint="address_id"
    )

    api.add_resource(
        AuthCustomerResource, "/auth/customers", endpoint="authenticate_customer"
    )
    api.add_resource(AuthAdminResource, "/auth/admins", endpoint="authenticate_admin")

    api.add_resource(
        CartResource, "/customers/<int:customer_id>/cart", endpoint="customer_cart"
    )

    api.add_resource(
        CartProductResource,
        "/customers/<int:customer_id>/cart/products/<int:product_id>",
        endpoint="customer_cart_product",
    )
