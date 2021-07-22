from functools import wraps
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
from flask import jsonify, make_response


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return make_response(jsonify(error="Admins only!"), 403)

        return decorator

    return wrapper


def customer_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if (
                claims.get("customer_id") == kwargs.get("customer_id")
                or claims["is_administrator"]
            ):
                return fn(*args, **kwargs)
            else:
                return make_response(jsonify(error="Resouce owner only!"), 403)

        return decorator

    return wrapper
