import uuid
from typing import List

from sqlalchemy import ARRAY, Column, String

from src.entities.services.name_validator import NameValidator

from .base import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True)
    name = Column(String)
    disciplines = Column(ARRAY(String))

    def __init__(
        self, id: str = None, name: str = None, disciplines: List[str] = None
    ) -> None:
        self.id = id or uuid.uuid4().__str__()
        self.name = NameValidator.validate(name)
        self.disciplines = disciplines or []
