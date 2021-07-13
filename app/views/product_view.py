from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.models.products_model import ProductsModel
from app.services.entity_services import EntityServices
from flask import jsonify
from datetime import datetime

class ProductResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("current_price", type=int)
        parser.add_argument("discount", type=int, required=True)
        parser.add_argument("amount_products", type=int)
        parser.add_argument("image_url", type=str, required=True)

        args = parser.parse_args()

        print(args)

        created_product = EntityServices.create_entity(ProductsModel, args)

        return jsonify(created_product), HTTPStatus.CREATED

    def get(self):
        list_product = EntityServices.get_all_entity(ProductsModel)

        return jsonify(list_customer), HTTPStatus.OK

class ProductIdResource(Resource):
    def get(self, product_id: int):
        found_product = EntityServices.get_entity_by_id(ProductsModel, product_id)

        return jsonify(found_product), HTTPStatus.OK

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

        found_product = EntityServices.get_entity_by_id(ProductsModel, product_id)

        updated_product = EntityServices.update_entity(found_product, args)

        return jsonify(updated_product), HTTPStatus.OK