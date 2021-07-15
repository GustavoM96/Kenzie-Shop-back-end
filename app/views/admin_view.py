from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from app.models.admin_model import AdminModel
from flask import jsonify, make_response


class AdminResource(Resource):
    def post(self):
        """Método ainda não cria customer"""

        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("password", type=str, required=True)

        args = parser.parse_args()

        created_admin = EntityServices.create_entity(AdminModel, args)

        return make_response(jsonify(created_admin), HTTPStatus.CREATED)
