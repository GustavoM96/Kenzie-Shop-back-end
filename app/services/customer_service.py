from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from app.models.cart_model import CartModel

from app.services.helper import add_all_commit


class CustomerServices:
    @staticmethod
    def create_customer(data: dict) -> CustomerModel:
        password_to_hash = data.pop("password")

        created_customer = CustomerModel(**data)
        created_customer.password = password_to_hash

        created_cart = CartModel(is_empty=False, total_price=0)

        created_customer.cart = created_cart

        add_all_commit([created_customer, created_cart])

        return created_customer
