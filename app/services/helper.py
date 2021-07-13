from flask_sqlalchemy.model import Model
from flask import current_app
from app.config.database import db


def add_commit(model: Model) -> None:
    session = db.session

    session.add(model)
    session.commit()


def add_all_commit(list_model: list[Model]) -> None:
    session = current_app.db.session

    session.add_all(list_model)
    session.commit()


def delete_commit(model: Model) -> None:
    session = current_app.db.session

    session.delete(model)
    session.commit()
