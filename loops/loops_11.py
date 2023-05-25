# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.

from random import randint

n = int(input('n = '))
m = int(input('m = '))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(m):
        arr_1.append(randint(1, 9))
    print(*arr_1)
    arr.append(arr_1)
result = 0
for arr_i in arr:
    for i in arr_i:
        if i == 7:
            result += 1
print(f'количество 7 в матрице равно: {result}')

# моя первая попытка
# n = int(input('размер матрицы n равен: '))
# m = int(input('размер матрицы m равен: '))
# matrix = [[randint(1, 60) for i in range(n)] for j in range(m)]
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] != 7:
#             print(matrix[i][j])
#         else:
#             print(f'кол-во 7 в матрице равно: {[i][j]}')
