from sqlalchemy import Column, ForeignKey, String

from src.entities.services.id_validator import IdValidator

from .base import Base


class Restriction(Base):
    __tablename__ = 'restrictions'

    id = Column(String, primary_key=True)
    teacher_id = ForeignKey('teachers.id')
    day = Column(String)
    time = Column(String)

    def __init__(
        self,
        id: str = None,
        teacher_id: str = None,
        day: str = None,
        time: str = None,
    ) -> None:
        self.id = IdValidator.validate(id)
        self.teacher_id = IdValidator.validate(teacher_id)
        self.day = day
        self.time = time
