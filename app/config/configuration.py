from flask import Flask
from environs import Env

env = Env()
env.read_env()


def init_app(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = env("SECRET_KEY")
