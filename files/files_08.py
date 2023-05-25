# Написать функции по работе с csv файлами в файле csv_utils.py. Чтение. Запись.
# Добавление записи(по позиции, по-умолчанию в конец). Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.

from csv_utils import create, reading, adding, deleting


def main():
    fields = ['name', 'price', 'count', 'description']
    rows = [['Sweets', 4, 10, 'best'], ['Cookies', 2, 100, 'Tasty'], ['Coca-cola', 60, 10, 'Zero']]
    create('testcsv.csv', fields, rows)

    print(reading('testcsv.csv'))
    adding('testcsv.csv', ['Fanta', 3, 10, 'Super'])
    print(reading('testcsv.csv'))
    deleting('testcsv.csv', 2)
    print(reading('testcsv.csv'))


if __name__ == '__main__':
    main()
