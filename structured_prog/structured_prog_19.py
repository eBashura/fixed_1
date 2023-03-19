# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.

from random import randint

my_matrix = []
n = int(input('n = '))
m = int(input('m = '))

my_matrix = [[randint(1, 100) for i in range(n)] for j in range(m)]
print(my_matrix)
for i in range(min(n, m)):
    max_num = max(my_matrix[i])
    r = my_matrix[i].index(max_num)
    print(f'макс значение равно: {max_num}')
    my_matrix[i][i], my_matrix[i][r] = my_matrix[i][r], my_matrix[i][i]
print(my_matrix)
