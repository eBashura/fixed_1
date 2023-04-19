# Создать файл book.py. Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.
# Ошибки вызываются при попытке создания неправильного объекта.
# Обработка происходит в пользовательском коде(в main).

class Book:

    def __init__(self, number_of_pages, year_of_publishing, author, price):
        self.number_of_pages = number_of_pages
        self.year_of_publishing = year_of_publishing
        self.author = author
        self.price = price
        if not isinstance(author, str):
            raise MyExceptionAuthorMustBeStr
        if not isinstance(number_of_pages, int) or not (year_of_publishing, int):
            raise MyExceptionPagerAndYearMustBeInt
        if not isinstance(price, int or float):
            raise MyExceptionPriceMustBeIntOrFloat


class MyException(Exception):
    def __init__(self, message='Problem with smth!'):
        super().__init__(message)


class MyExceptionAuthorMustBeStr(Exception):
    def __init__(self, message='Author must be in str mode!'):
        super().__init__(message)


class MyExceptionPagerAndYearMustBeInt(Exception):
    def __init__(self, message='Pages and year must be in int mode!'):
        super().__init__(message)


class MyExceptionPriceMustBeIntOrFloat(Exception):
    def __init__(self, message='Price must be in int or float mode!'):
        super().__init__(message)


def main():
    try:
        Book(555, 2023, 'Evgeny B', '97afa')
    except MyException as error:
        print(f'Some problems with {error}, check what is wrong!')
    else:
        print(f'Everything is good, well done!')
    finally:
        print(f'To create search of book, '
              f'number of pages must be int'
              f'year of publishing must be int'
              f'author must be str'
              f'price must be int or float')


if __name__ == '__main__':
    main()
