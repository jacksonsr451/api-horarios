from sqlalchemy import ARRAY, Column, String

Base = None


def init_table_teacher(base):
    global Base
    Base = base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    disciplines = Column(ARRAY(String))
