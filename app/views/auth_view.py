from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from app.models.admin_model import AdminModel
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import create_access_token
from flask import jsonify


class AuthCustomerResource(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        found_customer = EntityServices.get_entity_by_keys(
            CustomerModel, email=args["email"]
        )

        if found_customer.verify_password(args["password"]):
            refresh_token = create_refresh_token(identity=found_customer)

            access_token = create_access_token(
                identity=found_customer, additional_claims={"is_administrator": False}
            )

            return jsonify(access_token=access_token, refresh_token=refresh_token)


class AuthAdminResource(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        admin_customer = EntityServices.get_entity_by_keys(
            AdminModel, email=args["email"]
        )

        if admin_customer.verify_password(args["password"]):
            refresh_token = create_refresh_token(identity=admin_customer)

            access_token = create_access_token(
                identity=admin_customer, additional_claims={"is_administrator": True}
            )

            return jsonify(access_token=access_token, refresh_token=refresh_token)
