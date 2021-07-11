from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)
