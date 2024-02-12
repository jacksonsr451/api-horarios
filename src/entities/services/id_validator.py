import uuid

from src.entities.exceptions.id_exception import IdException


class IdValidator:
    @staticmethod
    def validate(id: str) -> str:
        return (
            id
            if id is not None and IdValidator.check_id_is_valid(id)
            else uuid.uuid4().__str__()
        )

    @staticmethod
    def check_id_is_valid(id: str) -> bool:
        try:
            uuid_obj = uuid.UUID(id, version=4)
            return str(uuid_obj) == id
        except ValueError:
            raise IdException(message='ID do not is valid')
