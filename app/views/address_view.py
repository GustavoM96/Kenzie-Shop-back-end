from flask_restful import Resource, reqparse
from datetime import datetime

from http import HTTPStatus
from app.services.entity_services import EntityServices

from app.models.address_model import AddressModel

from flask import jsonify, make_response
from sqlalchemy.exc import DataError

from app.exc import NotFoundEntityError
from app.services.auth_service import customer_required, admin_required


class AddressCustomerIdResource(Resource):
    @customer_required()
    def post(self, customer_id: int):

        parser = reqparse.RequestParser()

        parser.add_argument("customer_id", default=customer_id)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("number", type=int)
        parser.add_argument("complement", type=str)
        parser.add_argument("zipcode", type=str, required=True)
        parser.add_argument("city", type=str, required=True)
        parser.add_argument("state", type=str, required=True)

        args = parser.parse_args()

        try:
            create_address = EntityServices.create_entity(AddressModel, args)
            return make_response(jsonify(create_address), HTTPStatus.CREATED)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

    @customer_required()
    def get(self, customer_id: int):

        try:
            list_address = EntityServices.get_all_entity_by_keys(
                AddressModel, customer_id=customer_id
            )
            return make_response(jsonify(list_address), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND


class AddressIdCustomerIdResource(Resource):
    @customer_required()
    def get(self, customer_id: int, address_id: int):
        try:
            found_address = EntityServices.get_entity_by_id(AddressModel, address_id)
            return make_response(jsonify(found_address), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

    @customer_required()
    def patch(self, customer_id: int, address_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("number", type=int)
        parser.add_argument("complement", type=str)
        parser.add_argument("zipcode", type=str)
        parser.add_argument("city", type=str)
        parser.add_argument("state", type=str)
        parser.add_argument("updated_at", type=datetime, default=datetime.now())

        args = parser.parse_args()

        try:
            found_address = EntityServices.get_entity_by_id(AddressModel, address_id)
            updated_address = EntityServices.update_entity(found_address, args)
            return make_response(jsonify(updated_address), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY


class AddressIdResource(Resource):
    @admin_required()
    def get(self, address_id: int):
        try:
            found_address = EntityServices.get_entity_by_id(AddressModel, address_id)
            return make_response(jsonify(found_address), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND


class AddressResource(Resource):
    @admin_required()
    def get(self):

        list_addresses = EntityServices.get_all_entity(AddressModel)
        return make_response(jsonify(list_addresses), HTTPStatus.OK)
