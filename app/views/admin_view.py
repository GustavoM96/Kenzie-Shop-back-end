from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.admin_model import AdminModel
from flask import jsonify, make_response
from sqlalchemy.exc import IntegrityError
from app.services.helper import message_integrety_error
from sqlalchemy.exc import DataError


class AdminResource(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        try:
            created_admin = EntityServices.create_entity(AdminModel, args)
            return make_response(jsonify(created_admin), HTTPStatus.CREATED)

        except IntegrityError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY

        except DataError as error:
            return {"error": str(error.orig)}, HTTPStatus.UNPROCESSABLE_ENTITY
