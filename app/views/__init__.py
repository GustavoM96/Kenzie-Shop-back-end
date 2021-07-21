from .customer_view import CustomerResource, CustomerIdResource
from .product_view import ProductResource, ProductIdResource
from .cart_view import CartResource, CartProductResource
from .address_view import (
    AddressCustomerIdResource,
    AddressIdResource,
    AddressResource,
    AddressIdCustomerIdResource,
)
from .auth_view import AuthCustomerResource, AuthAdminResource
from .admin_view import AdminResource
from .order_view import OrderIdProductResource, OrderProductResource
from .send_email_view import EmailResource
