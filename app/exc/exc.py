from flask_sqlalchemy.model import Model
from sqlalchemy.exc import IntegrityError


class NotFoundEntityError(Exception):
    def __init__(self, model: Model) -> None:
        self.message = {"error": f"not found entity on {model.__tablename__}"}

        super().__init__(self.message)


class PasswordError(Exception):
    message_error = {"error": f"password or email incorrect"}

    def __init__(self) -> None:
        self.message = self.message_error

        super().__init__(self.message)