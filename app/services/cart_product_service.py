from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from app.models.product_model import ProductModel
from app.services.helper import add_all_commit


class CustomerServices:
    @staticmethod
    def calculate_total_price(current_price: float, quantity_product: int) -> float:
        return current_price * quantity_product

    @staticmethod
    def create_cart_product(
        quantity_product: int, customer_id: int, product_id: int
    ) -> CustomerModel:
        current_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        current_product = EntityServices.get_entity_by_id(ProductModel, product_id)

        current_price = current_product.current_price

        total_price = self.calculate_total_price(current_price, quantity_product)

        customer_cart = current_customer.cart
        cart_product_data: dict = {
            "cart_id": customer_cart.id,
            "product_id": product_id,
            "quantity_product": quantity_product,
            "total_price": total_price,
        }
        created_cart_product = EntityServices.create_entity(
            CartProductModel, cart_product_data
        )
        return created_customer
