from flask_restful import Resource, reqparse
from http import HTTPStatus
from app.models.customer_model import CustomerModel
from app.models.address_model import AddressModel
from app.models.order_model import OrderModel
import json
import requests
from app.services.entity_services import EntityServices
from flask import jsonify, make_response
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from app.services.auth_service import admin_required, customer_required
from app.exc import NotFoundEntityError
from sqlalchemy.exc import DataError


class EmailResource(Resource):
    @customer_required()
    def post(
        self,
        customer_id: int,
        address_id: int,
        order_id: int,
    ) -> None:

        customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)
        address = EntityServices.get_entity_by_id(AddressModel, address_id)
        order = EntityServices.get_entity_by_id(OrderModel, order_id)

        dict_to_request = {
            "personalizations": [
                {
                    "to": [{"email": "gustavo.hmessias96@gmail.com"}],
                    "dynamic_template_data": {
                        "subject": f"Compra do pedido nº{order.id} na Kenzie Shop",
                        "name": customer.name,
                        "order_id": order.id,
                        "total_price": order.total_price,
                        "was_paid": order.was_paid,
                        "products": "teste",
                        "street": address.name,
                        "number": address.number,
                        "complement": address.complement,
                        "city": address.city,
                        "state": address.state,
                    },
                }
            ],
            "from": {"email": "kenzie-shop@outlook.com"},
            "reply_to": {"email": "kenzie-shop@outlook.com"},
            "template_id": "d-d6eea5e222674addaff868eb32ef5624",
        }

        response = requests.post(
            f"https://api.sendgrid.com/v3/mail/send",
            data=json.dumps({**dict_to_request}),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "
                + "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",
            },
        )

        return response.text, response.status_code


# NÂO APAGAR   NÂO APAGAR
