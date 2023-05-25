"""Создать пакет school. Создать файл models.py. Создать базу school в postgre. Создать таблицу
Учебной группы(Group) с помощью sqlalchemy в декларативном стиле.
Группа характеризуется названием(name)."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_HOST = 'localhost'
DB_NAME = 'school'

e = create_engine(f'postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}', echo=True)
e = create_engine(f'postgresql://postgres:postgres@localhost/school', echo=True)

if not database_exists((e.url)):
    create_database(e.url)

Base = declarative_base()


class Group(Base):
    tablename = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def init(self, name):
        self.name = name


Base.metadata.create_all(e)
session = sessionmaker(bind=e)()
