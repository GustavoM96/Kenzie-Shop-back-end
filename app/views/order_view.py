from flask_restful import Resource, reqparse

from http import HTTPStatus
from app.services.entity_services import EntityServices

from app.models.order_product_model import OrderProductModel
from app.services.order_services import OrderServices
from app.models.order_model import OrderModel
from app.exc import NotFoundEntityError
from sqlalchemy.exc import IntegrityError
from app.services.helper import message_integrety_error
from flask import jsonify, make_response
from app.services.auth_service import customer_required


class OrderProductResource(Resource):
    @customer_required()
    def get(self, customer_id: int):

        list_order = EntityServices.get_all_entity_by_keys(
            OrderModel, customer_id=customer_id
        )

        return make_response(jsonify(list_order), HTTPStatus.OK)

    @customer_required()
    def post(self, customer_id: int):

        parser = reqparse.RequestParser()

        parser.add_argument("invoice_url", type=str)
        parser.add_argument("payment_type", type=str)

        args = parser.parse_args()

        order = OrderServices.create_order(customer_id, args)

        order_product = OrderServices.create_order_product(customer_id, order.id)

        return make_response(jsonify(order_product), HTTPStatus.CREATED)
