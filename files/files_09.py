# Использовать результаты files_08. Все функции описываются в csv_utils.py. Проверка работы функции осуществляется в files_09.py.
# Создать функцию подсчета полной суммы всех товаров.
# Создать функцию поиска самого дорогого товара.
# Создать функцию самого дешевого товара.
# Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)

from csv_utils import summ, max_price, min_price, minus, reading, adding, writing, deleting, create
from files_08 import *


def main():
    fields = ['name', 'price', 'count', 'description']
    rows = [['Sweets', 4, 10, 'best'], ['Cookies', 2, 100, 'Tasty'], ['Coca-cola', 60, 10, 'Zero']]
    create('testcsv.csv', fields, rows)


print(reading('testcsv.csv'))
print(summ('testcsv.csv'))
print(max_price('testcsv.csv'))
print(min_price('testcsv.csv'))
print(minus('testcsv.csv', 1))
