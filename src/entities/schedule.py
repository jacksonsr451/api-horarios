from sqlalchemy import Column, ForeignKey, String

Base = None


def init_table_discipline(base):
    global Base
    Base = base


class Schedule(Base):
    id = Column(String, primary_key=True)
    discipline_id = ForeignKey('discipline.id')
    day = Column(String)
    time = Column(String)
