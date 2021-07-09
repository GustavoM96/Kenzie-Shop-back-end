from flask import Flask

from app.config import load_configuration


def create_app():

    app = Flask(__name__)
    load_configuration(app)

    return app
