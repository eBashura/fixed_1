# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями. Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint
n = int(input('размер матрицы равен: '))
matrix = [[randint(3, 60) for i in range(n)] for j in range(n)]
sum = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] % 3 == 0:
            sum += matrix[i][j]
        print(matrix[i][j])
print(f'сумма элементов кратных 3 равна: {sum}')

# матрица выводится в один столбец, как починить?
