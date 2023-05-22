"""Создать файл sqlalchemy_04.py.
Написать программу: пользователь вводит данные о книге. Пользователю отображается введенная им информация.
Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
Если ответ да - выполнить метод .commit(), иначе - .rollback()"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Создание объекта Engine
engine = create_engine('URL: ')

# Получение соединения из объекта Engine
with engine.connect() as connection:
    # Создание транзакции
    transaction = connection.begin()
    title = input('title: ')
    pages = int(input('pages: '))
    author = input('author: ')
    price = float(input('price: '))
    release_year = int(input('release year: '))
    try:
        # Создание объекта типа `DDL` для выполнения запроса создания таблицы
        create_table_query = """
            create table Book (
                id integer primary key,
                title varchar,
                pages int,
                author varchar,
                price float,
                release_year int
            );
        """
        ddl = text(create_table_query)

        # Выполнение SQL-запроса с помощью метода `execute` на соединении
        connection.execute(ddl)

        # Фиксация транзакции после успешного выполнения
        transaction.commit()
    except SQLAlchemyError as e:
        # Обработка ошибки и откат транзакции в случае исключения
        transaction.rollback()
        