"""Создать файл book.py.
Создать базу book.db. Создать таблицу Book с помощью механизма описания таблиц sqlalchemy.
Атрибуты: id(integer primary key), title(varchar), pages(int), author(varchar), price(float), release_year(int) """

# Создать класс Book и сессию в файле book.py.
# Создать файл sqlalchemy_06. Импортировать Book и
# сессию из модуля book. Создать 3 книги с помощью сессии
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Book:
    def __init__(self, title, pages, author, price, release_year):
        # self.id = id
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


engine = create_engine('sqlite:///book.db', echo=True)

Session = sessionmaker(bind=engine)
session1 = Session()
