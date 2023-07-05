from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_HOST = 'localhost'
DB_NAME = 'school'