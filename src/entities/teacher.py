from typing import List

from flask_restx import fields
from sqlalchemy import ARRAY, Column, String

from src.adapters.controllers.api import api
from src.entities.services.id_validator import IdValidator
from src.entities.services.name_validator import NameValidator

from .base import Base

teacher_model = api.model(
    'Teacher',
    {
        'id': fields.String,
        'name': fields.String,
        'disciplines': fields.List(fields.String),
    },
)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True)
    name = Column(String)
    disciplines = Column(ARRAY(String))

    def __init__(
        self, id: str = None, name: str = None, disciplines: List[str] = None
    ) -> None:
        self.id = IdValidator.validate(id)
        self.name = NameValidator.validate(name)
        self.disciplines = disciplines or []
