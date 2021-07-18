from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.customer_model import CustomerModel
from app.models.admin_model import AdminModel
from flask_jwt_extended import create_access_token
from flask import jsonify
from app.exc import NotFoundEntityError, PasswordError


class AuthCustomerResource(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        try:
            found_customer = EntityServices.get_entity_by_keys(
                CustomerModel, email=args["email"]
            )

            if found_customer.verify_password(args["password"]):
                access_token = create_access_token(
                    identity=found_customer,
                    additional_claims={"is_administrator": False},
                )
                return {"access_token": access_token}, HTTPStatus.OK

        except NotFoundEntityError as _:
            return PasswordError.message_error, HTTPStatus.BAD_REQUEST

        except PasswordError as _:
            return PasswordError.message_error, HTTPStatus.BAD_REQUEST


class AuthAdminResource(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        try:
            admin_customer = EntityServices.get_entity_by_keys(
                AdminModel, email=args["email"]
            )

            if admin_customer.verify_password(args["password"]):
                access_token = create_access_token(
                    identity=admin_customer,
                    additional_claims={"is_administrator": True},
                )
                return {"access_token": access_token}, HTTPStatus.OK

        except NotFoundEntityError as _:
            return PasswordError.message_error, HTTPStatus.BAD_REQUEST

        except PasswordError as _:
            return PasswordError.message_error, HTTPStatus.BAD_REQUEST
