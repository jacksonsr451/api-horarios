from sqlalchemy import Column, ForeignKey, String

Base = None


def init_table_discipline(base):
    global Base
    Base = base


class Restriction(Base):
    id = Column(String, primary_key=True)
    teacher_id = ForeignKey('teachers.id')
    day = Column(String)
    time = Column(String)
