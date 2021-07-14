from flask_restful import Resource, reqparse
from datetime import datetime

from http import HTTPStatus
from app.services.entity_services import EntityServices

from app.models.address_model import AddressModel

from flask import jsonify, make_response


class AddressIdCustomerResource(Resource):
    def post(self, customer_id: int):
        """Método ainda não cria customer"""

        parser = reqparse.RequestParser()

        parser.add_argument("customer_id", default=customer_id)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("number", type=int)
        parser.add_argument("complement", type=str)
        parser.add_argument("zipcode", type=str, required=True)
        parser.add_argument("city", type=str, required=True)
        parser.add_argument("state", type=str, required=True)
        parser.add_argument("created_at", type=datetime)
        parser.add_argument("updated_at", type=datetime)

        args = parser.parse_args()

        """ modelo de criação de entidade"""
        create_address = EntityServices.create_entity(AddressModel, args)

        return make_response(jsonify(create_address), HTTPStatus.CREATED)

    def get(self, customer_id: int):
        list_address = [ad for ad in EntityServices.get_all_entity(AddressModel) if ad.customer_id == customer_id]

        return make_response(jsonify(list_address), HTTPStatus.OK)


class AdressIdResource(Resource):
    def get(self, address_id: int):
        found_address = EntityServices.get_entity_by_id(AddressModel, address_id)

        return make_response(jsonify(found_address), HTTPStatus.OK)

    def patch(self, address_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("number", type=int)
        parser.add_argument("complement", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("zipcode", type=str)
        parser.add_argument("city", type=str)
        parser.add_argument("state", type=str)
        parser.add_argument("update_at", type=datetime, default=datetime.now())

        args = parser.parse_args()

        found_address = EntityServices.get_entity_by_id(AddressModel, address_id)

        updated_address = EntityServices.update_entity(found_address, args)

        return make_response(jsonify(updated_address), HTTPStatus.OK)
