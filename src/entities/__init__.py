from sqlalchemy.ext.declarative import declarative_base

from .discipline import Discipline, init_table_discipline
from .restriction import Restriction, init_table_restriction
from .schedule import Schedule, init_table_schedule
from .teacher import Teacher, init_table_teacher

Base = declarative_base()

init_table_teacher(Base)
init_table_discipline(Base)
init_table_restriction(Base)
init_table_schedule(Base)
