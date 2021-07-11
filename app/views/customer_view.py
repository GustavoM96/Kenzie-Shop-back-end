from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from flask import jsonify


class CustomerResource(Resource):
    def post(self):
        """Método ainda não cria customer"""

        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str, required=True)
        parser.add_argument("last_name", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        """ modelo de criação de entidade"""
        created_user = EntityServices.create_entity(CustomerModel, args)

        return jsonify(created_user), HTTPStatus.CREATED

    def get(self):
        list_customer = EntityServices.get_all_entity(CustomerModel)

        return jsonify(list_customer), HTTPStatus.OK


class CustomerIdResource(Resource):
    def get(self, customer_id: int):
        found_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

        return jsonify(found_customer), HTTPStatus.OK

    def patch(self, customer_id: int):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)
        parser.add_argument("last_name", type=str)

        args = parser.parse_args()

        found_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

        updated_customer = EntityServices.update_entity(found_customer, args)

        return jsonify(updated_customer), HTTPStatus.OK
