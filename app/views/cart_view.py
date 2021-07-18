from collections import defaultdict
from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from app.models.cart_model import CartModel
from app.models.product_model import ProductModel
from app.models.carts_products_model import CartProductModel
from app.models.customer_model import CustomerModel
from app.services.entity_services import EntityServices
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from app.exc import NotFoundEntityError
from app.services.helper import message_integrety_error
from datetime import datetime


class CartResource(Resource):
    @jwt_required()
    def get(self, customer_id):
        try:
            current_customer = EntityServices.get_entity_by_id(
                CustomerModel, customer_id
            )
            customer_cart: CartModel = current_customer.cart

            list_products = EntityServices.get_all_entity_by_keys(
                CartProductModel, cart_id=customer_cart.id
            )
            return make_response(jsonify(list_products), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND


class CartProductResource(Resource):
    @jwt_required()
    def post(self, customer_id, product_id):

        quantity_product = int(request.args.get("quantity_product", 1))

        try:
            current_customer = EntityServices.get_entity_by_id(
                CustomerModel, customer_id
            )
            current_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            total_price = current_product.current_price * quantity_product
            customer_cart: CartModel = current_customer.cart
            cart_product: dict = {
                "cart_id": customer_cart.id,
                "product_id": product_id,
                "quantity_product": quantity_product,
                "total_price": total_price,
            }
            created_cart_product = EntityServices.create_entity(
                CartProductModel, cart_product
            )
            return make_response(jsonify(created_cart_product), HTTPStatus.CREATED)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except IntegrityError as _:
            return (
                message_integrety_error(CartProductModel),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

    def patch(self, customer_id, product_id):

        quantity_product = int(request.args.get("quantity_product", 1))

        try:
            current_customer = EntityServices.get_entity_by_id(
                CustomerModel, customer_id
            )
            current_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            updated_price = current_product.current_price * quantity_product
            customer_cart: CartModel = current_customer.cart
            data_cart_product: dict = {
                "quantity_product": quantity_product,
                "total_price": updated_price,
                "updated_at": datetime.now(),
            }
            current_cart_product = EntityServices.get_entity_by_keys(
                CartProductModel, cart_id=customer_cart.id, product_id=product_id
            )
            updated_cart_product = EntityServices.update_entity(
                current_cart_product, data_cart_product
            )
            return make_response(jsonify(updated_cart_product), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

    def delete(self, customer_id, product_id):
        try:
            current_customer = EntityServices.get_entity_by_id(
                CustomerModel, customer_id
            )
            customer_cart: CartModel = current_customer.cart
            current_cart_product = EntityServices.get_entity_by_keys(
                CartProductModel, cart_id=customer_cart.id, product_id=product_id
            )
            EntityServices.delete_entity(current_cart_product)
            return "", HTTPStatus.NO_CONTENT

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND
