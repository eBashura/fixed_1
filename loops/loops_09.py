# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

from random import randint

n = int(input('n = '))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(*arr_1)
    arr.append(arr_1)
# print(arr)

# n = int(input('размер матрицы равен: '))
# matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(matrix)
#
# матрица выводится в один столбец
