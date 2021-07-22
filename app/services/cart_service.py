from app.services.entity_services import EntityServices
from app.models.carts_products_model import CartProductModel
from app.models.customer_model import CustomerModel
from app.models.product_model import ProductModel
from datetime import datetime
from app.exc import NotFoundEntityError

from app.models.product_model import ProductModel
from flask_sqlalchemy.model import Model


class CartServices:
    @staticmethod
    def total_price_product(current_price: float, quantity_product: int) -> float:
        return current_price * quantity_product

    @staticmethod
    def update_total_price_cart(cart: Model, price_to_add: float):
        total_price = cart.total_price + price_to_add
        is_empty = False

        if not total_price:
            is_empty = True

        data = {"total_price": total_price, "is_empty": is_empty}

        cart = EntityServices.update_entity(cart, data)

    @staticmethod
    def get_cart(customer_id: int) -> dict:
        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        cart = customer.cart

        try:
            cart_dict = {
                "id": cart.id,
                "total_price": cart.total_price,
                "is_empty": cart.is_empty,
                "products": cart.carts_products,
            }
            return cart_dict
        except NotFoundEntityError as _:
            return {
                "id": cart.id,
                "total_price": cart.total_price,
                "is_empty": cart.is_empty,
                "products": [],
            }

    @classmethod
    def add_product_to_cart(
        cls, quantity_product: int, customer_id: int, product_id: int
    ) -> CartProductModel:

        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        product = EntityServices.get_entity_by_id(ProductModel, product_id)

        total_price = cls.total_price_product(product.current_price, quantity_product)

        cart_product_data = {
            "cart_id": customer.cart.id,
            "product_id": product_id,
            "quantity_product": quantity_product,
            "total_price": total_price,
        }
        created_cart_product = EntityServices.create_entity(
            CartProductModel, cart_product_data
        )

        cls.update_total_price_cart(customer.cart, total_price)

        return created_cart_product

    @classmethod
    def update_cart_product(
        cls, quantity_product: int, customer_id: int, product_id: int
    ) -> CartProductModel:

        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        product = EntityServices.get_entity_by_id(ProductModel, product_id)

        updated_price = cls.total_price_product(product.current_price, quantity_product)

        data_cart_product: dict = {
            "quantity_product": quantity_product,
            "total_price": updated_price,
            "updated_at": datetime.now(),
        }
        cart_product = EntityServices.get_entity_by_keys(
            CartProductModel, cart_id=customer.cart.id, product_id=product_id
        )

        change_price_to_cart = updated_price - cart_product.total_price

        cls.update_total_price_cart(customer.cart, change_price_to_cart)

        updated_cart_product = EntityServices.update_entity(
            cart_product, data_cart_product
        )
        return updated_cart_product

    @classmethod
    def delete_cart_product(cls, customer_id: int, product_id: int) -> None:

        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        cart = customer.cart

        cart_product = EntityServices.get_entity_by_keys(
            CartProductModel, cart_id=cart.id, product_id=product_id
        )

        change_price_to_cart = cart_product.total_price * -1

        cls.update_total_price_cart(cart, change_price_to_cart)

        EntityServices.delete_entity(cart_product)

    @classmethod
    def delete_all_cart_product(cls, customer_id: int) -> None:
        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        cart = customer.cart

        cart_product = EntityServices.get_all_entity_by_keys(
            CartProductModel, cart_id=cart.id
        )

        change_price_to_cart = cart.total_price * -1

        cls.update_total_price_cart(cart, change_price_to_cart)

        EntityServices.delete_all_entity(cart_product)
