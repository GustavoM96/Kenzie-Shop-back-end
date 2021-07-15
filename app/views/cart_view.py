from collections import defaultdict
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from app.models.cart_model import CartModel
from app.models.product_model import ProductModel
from app.models.carts_products_model import CartProductModel
from app.models.customer_model import CustomerModel
from app.services.entity_services import EntityServices
from http import HTTPStatus


class CartResource(Resource):
    def get(self, customer_id):

        current_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

        customer_cart: CartModel = current_customer.cart

        all_carts_products = EntityServices.get_all_entity(CartProductModel)

        current_cart_product = [
            cart_product
            for cart_product in all_carts_products
            if cart_product.cart_id == customer_cart.id
        ]

        return make_response(jsonify(current_cart_product), HTTPStatus.OK)


class CartProductResource(Resource):
    def post(self, customer_id, product_id):
        parser = reqparse.RequestParser()

        parser.add_argument("quantity_product", type=int, default=1)

        args = parser.parse_args()

        current_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

        current_product = EntityServices.get_entity_by_id(ProductModel, product_id)

        total_price = current_product.current_price * args["quantity_product"]

        customer_cart: CartModel = current_customer.cart

        cart_product: dict = {
            "cart_id": customer_cart.id,
            "product_id": product_id,
            "quantity_product": args["quantity_product"],
            "total_price": total_price,
        }

        created_cart_product = EntityServices.create_entity(
            CartProductModel, cart_product
        )

        return make_response(jsonify(created_cart_product), HTTPStatus.CREATED)
