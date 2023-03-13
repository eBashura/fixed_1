# Дана целочисленная матрица А[n,m]. Посчитать количество элементов матрицы, превосходящих среднее
# арифметическое значение элементов матрицы и сумма индексов которых четна.

# for i, n in enumerate(range(10, 15)):
#     print(f'i = {i}, n = {n}')

from random import randint

n = int(input('n = '))
m = int(input('m = '))
arr = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
print(arr)

sum = 0
count = 0
for arr_i in arr:
    for i in arr_i:
        sum += i
        count += 1
avg = sum / count
print(avg)
count_2 = 0
for i, arr_i in enumerate(arr):
    for r, number in enumerate(arr_i):
        if number > avg and ((i+r) % 2) == 0:
            count_2 += 1
print(count_2)

