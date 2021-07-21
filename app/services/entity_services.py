from app.services.helper import add_all_commit, add_commit, delete_commit
from flask_sqlalchemy.model import Model
from app.exc import NotFoundEntityError


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

        if not found_entity:
            raise NotFoundEntityError(model)

        return found_entity

    @staticmethod
    def get_entity_by_keys(model: Model, **kargs) -> Model:
        found_entity = model.query.filter_by(**kargs).first()

        if not found_entity:
            raise NotFoundEntityError(model)

        return found_entity

    @staticmethod
    def get_all_entity_by_keys(model: Model, **kargs) -> list[Model]:
        found_list_entity = model.query.filter_by(**kargs).all()

        if not found_list_entity:
            raise NotFoundEntityError(model)

        return found_list_entity

    @staticmethod
    def create_entity(model: Model, data: dict) -> Model:
        entity = model(**data)

        add_commit(entity)

        return entity

    @staticmethod
    def create_all_entity(model: Model, data_list: list) -> Model:
        list_entity = [model(**data) for data in data_list]

        add_all_commit(list_entity)

        return list_entity

    @staticmethod
    def update_entity(entity: Model, data: dict) -> Model:
        update_entity = entity

        for key, value in data.items():
            if value != None:
                setattr(update_entity, key, value)

        add_commit(update_entity)

        return entity

    @staticmethod
    def delete_entity(entity: Model) -> None:
        deleted_entity = entity

        delete_commit(entity)

        return None

    @staticmethod
    def delete_all_entity(list_entity: list[Model]) -> None:
        deleted_list_entity = list_entity

        for entity in list_entity:
            delete_commit(entity)

        return None
