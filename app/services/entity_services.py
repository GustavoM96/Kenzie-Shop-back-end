from app.services.helper import add_all_commit, add_commit, delete_commit
from flask_sqlalchemy.model import Model


class EntityServices:
    """
    Esse é um tipo de documentação Python usado no padrão pep8, use o __doc__ e retornará esses dados:
    Essa classe tem o objetivo de fazer um CRUD de entidades(objetos da classe Model)
    """

    @staticmethod
    def get_all_entity(model: Model) -> list[Model]:
        list_entity = model.query.all()

        return list_entity

    @staticmethod
    def get_entity_by_id(model: Model, entity_id: int) -> Model:
        found_entity = model.query.get(entity_id)

        return found_entity

    @staticmethod
    def create_entity(model: Model, data: dict) -> Model:
        entity = model(**data)

        add_commit(entity)

        return entity

    @staticmethod
    def update_entity_by_id(entity: Model, entity_id: int, data: dict) -> Model:
        updated_entity = model.query.get(entity_id)

        for key, value in data.items():
            setattr(updated_entity, key, value)

        add_commit(updated_entity)

        return updated_entity

    @staticmethod
    def delete_entity_by_id(entity: Model) -> None:
        found_entity = model.query.get(product_id)

        delete_commit(found_entity)

        return None
