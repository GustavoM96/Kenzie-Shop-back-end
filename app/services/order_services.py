from app.models.cart_model import CartModel
from app.models.customer_model import CustomerModel
from app.models.order_model import OrderModel
from app.models.order_product_model import OrderProductModel

from app.services.cart_service import CartServices
from app.services.entity_services import EntityServices


class OrderServices:
    @staticmethod
    def create_order(customer_id: int, data: dict):
        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

        cart = EntityServices.get_entity_by_id(CartModel, customer.cart_id)

        data["total_price"] = cart.total_price
        data["customer_id"] = customer_id

        order = EntityServices.create_entity(OrderModel, data)
        return order

    @staticmethod
    def create_order_product(customer_id: int, order_id: int):

        cart = CartServices.get_cart(customer_id)

        list_data = []

        for item in cart["products"]:
            data = {
                "order_id": order_id,
                "product_id": item.product.id,
                "sold_price": item.product.current_price,
                "quantity_product": item.quantity_product,
                "total_price": item.total_price,
            }
            list_data.append(data)

        order_product = EntityServices.create_all_entity(OrderProductModel, list_data)

        return order_product

    @staticmethod
    def get_order_by_id(order_id: int):

        order = EntityServices.get_entity_by_id(OrderModel, order_id)

        order_dict = {
            "id": order.id,
            "invoice_url": order.invoice_url,
            "total_price": order.total_price,
            "was_paid": order.was_paid,
            "payment_type": order.payment_type,
            "payment_day": order.payment_day,
            "products": order.orders_products,
        }

        return order_dict
