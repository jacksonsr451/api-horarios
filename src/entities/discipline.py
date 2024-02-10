from sqlalchemy import ARRAY, Column, String

Base = None


def init_table_discipline(base):
    global Base
    Base = base


class Discipline:
    id = Column(String, primary_key=True)
    name = Column(String)
    schedules = Column(ARRAY(String))
