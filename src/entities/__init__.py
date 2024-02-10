from sqlalchemy.ext.declarative import declarative_base

from .teacher import Teacher, init_table_teacher

Base = declarative_base()

init_table_teacher(Base)
