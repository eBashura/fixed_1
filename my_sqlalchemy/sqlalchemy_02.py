# Создать файл sqlalchemy_02.py. Создать соединение к базе sa_test.db. Создать 5 книг с помощью sqlalchemy.

from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    insert_query = """
        INSERT INTO Book(title, pages, author, price, release_year)
            values('harry', 600, Rowling, 35, 2001),
            ('harry potter', 600, Rowling, 35, 2004),
            ('harry and fire tour', 600, Rowling, 35, 2007),
            ('harry and voldemort', 600, Rowling, 35, 2012),
            ('harry and death path', 600, Rowling, 35, 2016);
    """
    query = text(insert_query)

    connection.execute(query)
    connection.commit()
