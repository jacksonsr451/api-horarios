from sqlalchemy.ext.declarative import declarative_base

from .discipline import Discipline, init_table_discipline
from .restriction import Restriction, init_table_restriction
from .teacher import Teacher, init_table_teacher

Base = declarative_base()

init_table_teacher(Base)
init_table_discipline(Base)
init_table_restriction(Base)
