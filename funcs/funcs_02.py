# Написать программу для работы с матрицами:
# 1)Создание
# 2)Вывод
# 3)Сумма всех элементов
# 4)Нахождение максимального элемента
# 5)Нахождение минимального элемента.

from random import randint


def create_matrix(n: int) -> list:
    matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    # matrix = []
    # for _ in range(n):
    #     arr_2 = []
    #     for _ in range(n):
    #         arr_2.append(randint(1, 10))
    #     matrix.append(arr_2)
    return matrix


def print_matrix(matrix: list) -> None:
    for arr in matrix:
        print(arr)


def sum_matrix(matrix: list) -> int:
    sum = 0
    for arr in matrix:
        for i in arr:
            sum += i
    print(f'сумма элементов матрицы: {sum}')
    # for arr in matrix:
    #     sum += sum(arr)
    # result = sum([sum(arr) for arr in matrix])


def max_num(matrix):
    list_of_max_elem = []
    for arr in matrix:
        max_elem_in_arr = max(arr)
        list_of_max_elem.append(max_elem_in_arr)
    max_number = max(list_of_max_elem)
    return max_number
    # return max([max(arr) for arr in matrix])


def min_num(matrix):
    list_of_min_elem = []
    for arr in matrix:
        min_elem_in_arr = min(arr)
        list_of_min_elem.append(min_elem_in_arr)
    min_number = min(list_of_min_elem)
    return min_number


def main():
    matrix = create_matrix(3)
    print_matrix(matrix)
    sum_matrix(matrix)
    max_number = max_num(matrix)
    print(f'максимальный элемент: {max_number}')
    min_number = min_num(matrix)
    print(f'минимальный элемент: {min_number}')


if __name__ == '__main__':
    main()
