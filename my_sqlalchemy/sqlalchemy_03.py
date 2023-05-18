from sqlalchemy import create_engine, text


def find_books_by_year():
    engine = create_engine('sqlite:///sa_test.db')
    with engine.connect() as connection:
        year = int(input('введите год: '))
        select_query_text = f"""SELECT * FROM Book WHERE release_year < {year}"""
        query = text(select_query_text)
        data = list(connection.execute(query))
        if len(data) != 0:
            for book in data:
                print(book)
        else:
            print('Not Found!')


def main():
    find_books_by_year()


if __name__ == '__main__':
    main()
