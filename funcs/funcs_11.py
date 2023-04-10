# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1), и False
# в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
# ных чисел. С помощью функции is_power_n найти количество степеней числа n в данном наборе.

import math
from random import randint

def is_power_n(k:int, n:int):
    if math.log(k, n) % 1 == 0:
        return True
    else:
        return False


def main():
    number = int(input('n = '))
    arr = [randint(1, 10) for i in range(10)]
    print(arr)
    counter = 0
    for i in arr:
        if is_power_n(i, number):
            counter += 1
    print(f'кол-во степеней {counter}')

if __name__ == '__main__':
    main()


#2й
# def is_power_n(k: int, n: int) -> bool:
#     test_k = 0
#     counrer = 1
#     while test_k <= k:
#         if test_k == k:
#             return True
#         test_k = n ** counrer
#         counrer += 1
#
#
# print(is_power_n(10, 3))