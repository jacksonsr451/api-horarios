from src.entities.exceptions.name_exception import NameException


class NameValidator:
    @staticmethod
    def validate(name: str) -> str:
        if not name:
            raise NameException('Name is required')
        return name
