from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.models.product_model import ProductModel
from app.services.entity_services import EntityServices
from flask import jsonify, make_response
from datetime import datetime


class ProductResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("current_price", type=float)
        parser.add_argument("discount", type=int, required=True)
        parser.add_argument("amount_products", type=int)
        parser.add_argument("image_url", type=str, required=True)

        args = parser.parse_args()

        created_product = EntityServices.create_entity(ProductModel, args)

        return make_response(jsonify(created_product), HTTPStatus.CREATED)

    def get(self):
        list_product = EntityServices.get_all_entity(ProductModel)

        return make_response(jsonify(list_product), HTTPStatus.OK)


class ProductIdResource(Resource):
    def get(self, product_id: int):
        found_product = EntityServices.get_entity_by_id(ProductModel, product_id)

        return make_response(jsonify(found_product), HTTPStatus.OK)

    def patch(self, product_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("current_price", type=int)
        parser.add_argument("discount", type=int)
        parser.add_argument("amount_products", type=int)
        parser.add_argument("updated_at", type=datetime)
        parser.add_argument("image_url", type=str)

        args = parser.parse_args()

        found_product = EntityServices.get_entity_by_id(ProductModel, product_id)

        updated_product = EntityServices.update_entity(found_product, args)

        return make_response(jsonify(updated_product), HTTPStatus.OK)
