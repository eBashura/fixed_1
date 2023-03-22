# Написать программу для работы с матрицами:
# 1)Создание
# 2)Вывод
# 3)Сумма всех элементов
# 4)Нахождение максимального элемента
# 5)Нахождение минимального элемента.

from random import randint


def create_matrix():
    arr = [randint(1, 10) for _ in range(5)]
    return arr


def print_matrix(arr):
    print(arr)


def sum_matrix(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def max_matrix(arr):
    return max(arr)


def min_matrix(arr):
    return min(arr)


def main():
    matrix = create_matrix()
    print_matrix(matrix)
    print(sum_matrix(matrix))
    print(max_matrix(matrix))
    print(min_matrix(matrix))


if __name__ == "__main__":
    main()
