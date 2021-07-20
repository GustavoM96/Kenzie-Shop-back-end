from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.models.product_model import ProductModel
from app.services.entity_services import EntityServices
from app.services.helper import message_integrety_error
from flask import jsonify, make_response
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from app.services.auth_service import admin_required, customer_required
from app.exc import NotFoundEntityError


class ProductResource(Resource):
    @admin_required()
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str, required=True)
        parser.add_argument("description", type=str, required=True)
        parser.add_argument("current_price", type=float, required=True)
        parser.add_argument("discount", type=int, required=True)
        parser.add_argument("amount_products", type=int, required=True)
        parser.add_argument("image_url", type=str, required=True)

        args = parser.parse_args()

        try:
            created_product = EntityServices.create_entity(ProductModel, args)
            return make_response(jsonify(created_product), HTTPStatus.CREATED)

        except IntegrityError as _:
            return make_response(
                message_integrety_error(ProductModel),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

    def get(self):
        list_product = EntityServices.get_all_entity(ProductModel)

        return make_response(jsonify(list_product), HTTPStatus.OK)


class ProductIdResource(Resource):
    def get(self, product_id: int):
        try:
            found_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            return make_response(jsonify(found_product), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return make_response(error.message, HTTPStatus.NOT_FOUND)

    @admin_required()
    def patch(self, product_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("current_price", type=int)
        parser.add_argument("discount", type=int)
        parser.add_argument("amount_products", type=int)
        parser.add_argument("updated_at", type=datetime, default=datetime.now())
        parser.add_argument("image_url", type=str)

        args = parser.parse_args()

        try:
            found_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            updated_product = EntityServices.update_entity(found_product, args)
            return make_response(jsonify(updated_product), HTTPStatus.OK)

        except IntegrityError as _:
            return (
                message_integrety_error(ProductModel),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

    @admin_required()
    def delete(self, product_id: int):

        try:
            found_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            EntityServices.delete_entity(found_product)
            return "", HTTPStatus.NO_CONTENT

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND
