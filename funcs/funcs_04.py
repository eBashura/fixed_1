# Реализовать функцию возвращающую матрицу. На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).
from random import randint


def create_matrix(n, random_from=1, random_to=9):
    return [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]


def create_matrix2(n, random_from=1, random_to=9):
    matrix = []
    for _ in range(n):
        matrix_2 = []
        for _ in range(n):
            matrix_2.append(randint(random_from, random_to))
            matrix.append(matrix_2)
    return matrix


def main():
    print(create_matrix(3))
    print(create_matrix2(3))
    matrix = create_matrix2(3)
    for arr in matrix:
        print(arr)


if __name__ == '__main__':
    main()

# def matrix(n: int) -> list:
#     my_matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
#     return my_matrix
#
#
# def main():
#     print(matrix(3))
#
#
# if __name__ == '__main__':
#     main()