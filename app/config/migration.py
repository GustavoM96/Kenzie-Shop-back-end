from flask_migrate import Migrate
from flask import Flask


mg = Migrate()


def init_app(app: Flask) -> None:
    mg.init_app(app, app.db)
