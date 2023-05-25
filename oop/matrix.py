# Создать файл matrix.py. Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
# Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b),
# по-умолчанию(матрица 5 на 5 где все элементы равны нулю), копирования) , переопределить магический метод __str__ для красивого вывода.
# Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами
from abc import ABC
from random import randint


class Matrix:
    def __init__(self, data=None, n=5, m=5, random_start=0, random_finish=0):
        if data:
            self.__n = data.__n
            self.__m = data.__m
            self.__data = data.__data
        else:
            self.__n = data.__n
            self.__m = data.__m
            self.__data = [[randint(random_start, random_finish)
                            for _ in range(m)] for _ in range(n)]
# доделать это и 20!!!
