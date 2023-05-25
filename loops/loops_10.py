# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями. Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input('n = '))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(*arr_1)
    arr.append(arr_1)
sum = 0
for arr_i in arr:
    for i in arr_i:
        if i % 3 == 0:
            sum += i
print(f'сумма элементов кратных 3: {sum}')

# n = int(input('размер матрицы равен: '))
# matrix = [[randint(3, 60) for i in range(n)] for j in range(n)]
# sum = 0
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] % 3 == 0:
#             sum += matrix[i][j]
#         print(matrix[i][j])
# print(f'сумма элементов кратных 3 равна: {sum}')
