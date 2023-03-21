# Реализовать функцию возвращающую матрицу. На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).
from random import randint


def matrix(n):
    my_matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    print(my_matrix)
    return my_matrix


matrix(int(input("n = ")))
