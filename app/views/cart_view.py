from flask import jsonify, make_response, request
from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.exc import NotFoundEntityError
from app.services.auth_service import customer_required
from app.services.cart_service import CartServices
from sqlalchemy.exc import DataError


class CartResource(Resource):
    @customer_required()
    def get(self, customer_id):
        try:
            cart_dict = CartServices.get_cart(customer_id)
            return make_response(jsonify(cart_dict), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

    @customer_required()
    def delete(self, customer_id):
        try:
            CartServices.delete_all_cart_product(customer_id)
            return "", HTTPStatus.NO_CONTENT

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND


class CartProductResource(Resource):
    @customer_required()
    def post(self, customer_id, product_id):

        quantity_product = int(request.args.get("quantity_product", 1))

        try:
            created_cart_product = CartServices.add_product_to_cart(
                quantity_product, customer_id, product_id
            )
            return make_response(jsonify(created_cart_product), HTTPStatus.CREATED)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except IntegrityError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

    @customer_required()
    def patch(self, customer_id, product_id):

        quantity_product = int(request.args.get("quantity_product", 0))

        if not quantity_product:
            return {
                "error": "there is not parameter Url (quantity_product)"
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        try:
            updated_cart_product = CartServices.update_cart_product(
                quantity_product, customer_id, product_id
            )
            return make_response(jsonify(updated_cart_product), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

    @customer_required()
    def delete(self, customer_id, product_id):
        try:
            CartServices.delete_cart_product(customer_id, product_id)
            return "", HTTPStatus.NO_CONTENT

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND
