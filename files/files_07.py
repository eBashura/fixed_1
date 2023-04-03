# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл

import json
from random import randint

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/json.txt', 'w') as my_file:
    matrix = [[randint(1, 10) for _ in range(3)] for _ in range(3)]
    data = json.dumps(matrix)
    my_file.write(data)

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/json.txt') as my_file, open(
        '/home/evgeny/PycharmProjects/fixed_1/files/test_files/json_new.txt', 'w') as json_file:
    data = json.load(my_file)
    for index_row, row in enumerate(data):
        for index_number, number in enumerate(row):
            if number % 2 == 0:
                data[index_row][index_number] = 0
    json.dump(data, json_file)
