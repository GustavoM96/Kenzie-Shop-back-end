from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from flask import jsonify, make_response
from app.services.customer_service import CustomerServices
from app.services.auth_service import admin_required, customer_required
from sqlalchemy.exc import IntegrityError
from app.exc import NotFoundEntityError
from app.services.helper import message_integrety_error
from sqlalchemy.exc import DataError
from datetime import datetime


class CustomerResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str, required=True)
        parser.add_argument("last_name", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        try:
            created_user = CustomerServices.create_customer(args)
            return make_response(jsonify(created_user), HTTPStatus.CREATED)

        except IntegrityError as error:
            return ({"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY)

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

    @admin_required()
    def get(self):
        list_customer = EntityServices.get_all_entity(CustomerModel)

        return make_response(jsonify(list_customer), HTTPStatus.OK)


class CustomerIdResource(Resource):
    @customer_required()
    def get(self, customer_id: int):

        try:
            found_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
            return make_response(jsonify(found_customer), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

    @customer_required()
    def patch(self, customer_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("last_name", type=str)
        parser.add_argument("updated_at", type=datetime, default=datetime.now())

        args = parser.parse_args()

        try:
            found_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
            updated_customer = EntityServices.update_entity(found_customer, args)
            return make_response(jsonify(updated_customer), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

        except IntegrityError as error:
            return ({"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY)
