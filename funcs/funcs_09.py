# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать функцию.
# Подсказка: для хранения данных использовать словарь. Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in
from random import randint


def equal_number(arr: list) -> dict:
    dict = {}
    for i in set(arr):
        dict[i] = arr.count(i)
    return dict


# def counter_NUMBERS(arr: list) -> dict:
#     dict = {}
#     for i in arr:
#         if dict.get(i):
#             dict[i] = dict[i] + 1
#         else:
#             dict[i] = 1
#     return dict


def main():
    arr = [randint(1, 10) for _ in range(6)]
    print(arr)
    print(equal_number(arr))


if __name__ == '__main__':
    main()