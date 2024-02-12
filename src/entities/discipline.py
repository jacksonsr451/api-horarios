import uuid
from typing import List

from sqlalchemy import ARRAY, Column, String

from src.entities.services.id_validator import IdValidator
from src.entities.services.name_validator import NameValidator

from .base import Base


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(String, primary_key=True)
    name = Column(String)
    schedules = Column(ARRAY(String))

    def __init__(
        self, id: str = None, name: str = None, schedules: List[str] = None
    ) -> None:
        self.id = IdValidator.validate(id)
        self.name = NameValidator.validate(name=name)
        self.schedules = schedules or []
