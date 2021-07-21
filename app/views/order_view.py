from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.services.entity_services import EntityServices
from datetime import datetime
from app.services.order_services import OrderServices
from app.models.order_model import OrderModel
from flask import jsonify, make_response
from app.services.auth_service import customer_required
from app.services.cart_service import CartServices
from app.services.email_services import EmailService


class OrderProductResource(Resource):
    @customer_required()
    def get(self, customer_id: int):

        list_order = EntityServices.get_all_entity_by_keys(
            OrderModel, customer_id=customer_id
        )

        return make_response(jsonify(list_order), HTTPStatus.OK)

    @customer_required()
    def post(self, customer_id: int, address_id: id):

        parser = reqparse.RequestParser()

        parser.add_argument("invoice_url", type=str)
        parser.add_argument("payment_type", type=str)

        args = parser.parse_args()

        order = OrderServices.create_order(customer_id, args)

        order_product = OrderServices.create_order_product(customer_id, order.id)

        EmailService.send_email(customer_id, address_id, order.id)

        CartServices.delete_all_cart_product(customer_id)

        return make_response(jsonify(order_product), HTTPStatus.CREATED)


class OrderIdProductResource(Resource):
    @customer_required()
    def get(self, customer_id: int, order_id: int):

        order = OrderServices.get_order_by_id(order_id)

        return make_response(jsonify(order), HTTPStatus.OK)

    @customer_required()
    def patch(self, customer_id: int, order_id: int):

        parser = reqparse.RequestParser()

        parser.add_argument("payment_type", type=str, required=True)
        parser.add_argument("invoice_url", type=str)

        args = parser.parse_args()

        args["payment_day"] = datetime.now()
        args["was_paid"] = True

        order = EntityServices.get_entity_by_id(OrderModel, order_id)

        updated_order = EntityServices.update_entity(order, args)

        return make_response(jsonify(updated_order), HTTPStatus.OK)
