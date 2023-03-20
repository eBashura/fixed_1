# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.

from random import randint

n = int(input('n = '))
m = int(input('m = '))

my_matrix = [[randint(1, 100) for i in range(n)] for j in range(m)]
print(my_matrix)
for arr in my_matrix:
    print(arr)

for i in range(min(n, m)):
    max_num = max(my_matrix[i])
    r = my_matrix[i].index(max_num)
    print(f'макс значение равно: {max_num}')
    my_matrix[i][i], my_matrix[i][r] = my_matrix[i][r], my_matrix[i][i]
for arr in my_matrix:
    print(arr)

# for index, number in enumerate(my_matrix):
#     max_element = max(number)
#     index_max_elem = my_matrix.index(max_element)
#     my_matrix[index], my_matrix[index_max_elem] = my_matrix[index_max_elem], my_matrix[index]
# print(my_matrix)
