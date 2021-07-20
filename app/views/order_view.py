from datetime import datetime
from flask_restful import Resource, reqparse

from http import HTTPStatus
from app.services.entity_services import EntityServices

from app.models.order_product_model import OrderProductModel
from app.models.product_model import ProductModel
from app.models.customer_model import CustomerModel
from app.models.cart_model import CartModel
from app.models.carts_products_model import CartProductModel
from app.models.address_model import AddressModel
from app.models.shipment_model import ShipmentModel
from app.models.order_model import OrderModel

from app.exc import NotFoundEntityError
from sqlalchemy.exc import IntegrityError
from app.services.helper import message_integrety_error
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required

class OrderProductIdResource(Resource):
    @jwt_required()
    def get(self, customer_id: int, order_id:int):
        try:
            list_order_product = EntityServices.get_all_entity_by_keys(
                OrderProductModel, order_id=order_id
            )
            return make_response(jsonify(list_order_product), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

class OrderIdProductIdResource(Resource):
    @jwt_required()
    def post(self, order_id: int, product_id: int):
        quantity_product = int(request.args.get("quantity_product", 1))
        
        try:   
            current_product = EntityServices.get_entity_by_id(ProductModel, product_id)
            total_price = current_product.current_price * quantity_product

            data: dict = {
                "order_id": order_id,
                "product_id": product_id,
                "sold_price": current_product.current_price,
                "quantity_product": quantity_product,
                "total_price": total_price
            }

            create_order_product = EntityServices.create_entity(OrderProductModel, data)

            return make_response(jsonify(create_order_product), HTTPStatus.CREATED)
        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except IntegrityError as _:
            return (
                message_integrety_error(OrderProductModel),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )


class OrderResource(Resource):
    @jwt_required()
    def get(self, customer_id:int):
        try:
            list_order = EntityServices.get_all_entity(
                OrderProductModel, customer_id=customer_id
            )
            return make_response(jsonify(list_order), HTTPStatus.OK)

        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND
    @staticmethod
    def _shipping():
            parser = reqparse.RequestParser()
    
            parser.add_argument("code_correios", type=str, required=True)
            parser.add_argument("shipping_price", type=float, required=True)
            parser.add_argument("status", type=str)
            parser.add_argument("chegada_data", type=str)
            parser.add_argument("saida_data", type=str)
            parser.add_argument("address_id", type=int, required=True)
           
            args = parser.parse_args()

            current_address: AddressModel = EntityServices.get_entity_by_id(AddressModel, args["address_id"])

            args["name"] = current_address.name
            args["number"] = current_address.number
            args["complement"] = current_address.complement
            args["cep"] = current_address.zipcode
            args["city"] = current_address.city
            args["state"] = current_address.state
    
            try:
                current_shipping = EntityServices.create_entity(ShipmentModel, args)
                return current_shipping
    
            except IntegrityError as _:
                return (
                    message_integrety_error(CustomerModel),
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

    @jwt_required()
    def post(self, customer_id:int):
        try:
            current_customer = EntityServices.get_entity_by_id(CustomerModel, customer_id)

            current_cart_product = EntityServices.get_all_entity_by_keys(CartProductModel, cart_id=current_customer.cart_id)

            current_cart = EntityServices.get_entity_by_id(CartModel, current_customer.cart_id)

            current_shipping = self._shipping()

            total_price = current_cart.total_price

            total = total_price * current_shipping["shipping_price"]
            
            parser = reqparse.RequestParser()

            parser.add_argument("customer_id", default=customer_id)
            parser.add_argument("nota_fiscal_url", type=str)
            parser.add_argument("type_payment", type=str, required=True)
            parser.add_argument("payment_day", type=datetime, default=datetime.now())

            args = parser.parse_args()
            args["total_price"] = total_price
            args["total"] = total
            args["shipping_id"] = current_shipping.id

            create_order = EntityServices.create_entity(OrderModel, args)

            OrderProductIdResource.post(create_order.id, current_cart_product.product_id)

            return make_response(jsonify(create_order), HTTPStatus.CREATED)
        except NotFoundEntityError as error:
            return error.message, HTTPStatus.NOT_FOUND

        except IntegrityError as _:
            return (
                message_integrety_error(OrderProductModel),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )


    