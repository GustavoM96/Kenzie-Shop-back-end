from flask import Flask
from . import database, configuration, migration, jwt, api
from flask_cors import CORS


def load_configuration(app: Flask) -> None:
    CORS(app, resources={r"/*": {"origins": "*"}})
    configuration.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)
    api.init_app(app)
