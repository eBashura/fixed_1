# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

from random import randint
n = int(input('размер матрицы равен: '))
matrix = [[randint(1, 10) for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j])

# матрица выводится в один столбец