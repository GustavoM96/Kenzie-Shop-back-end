from flask import Flask
from . import database, configuration, migration, blueprint, jwt


def load_configuration(app: Flask) -> None:

    configuration.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)
    blueprint.init_app(app)
