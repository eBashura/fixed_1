# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.

from random import randint
n = int(input('размер матрицы n равен: '))
m = int(input('размер матрицы m равен: '))
matrix = [[randint(1, 60) for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 7:
            print(matrix[i][j])
        else:
            print(f'кол-во 7 в матрице равно: {[i][j]}')

# с этим надо разобраться, не понимаю как вывести кол-во семерок в матрице

