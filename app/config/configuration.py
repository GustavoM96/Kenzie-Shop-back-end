from flask import Flask
from environs import Env

from datetime import timedelta

env = Env()
env.read_env()


def init_app(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = env("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=60)
    app.config["CORS_HEADERS"] = "Content-Type"
